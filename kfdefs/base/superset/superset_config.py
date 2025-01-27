import os
from flask_appbuilder.security.manager import AUTH_DB, AUTH_LDAP

MAPBOX_API_KEY = os.getenv('MAPBOX_API_KEY', '')
SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@supersetdb:5432/{}".format(os.environ['POSTGRESQL_USERNAME'], os.environ['POSTGRESQL_PASSWORD'], os.environ['POSTGRESQL_DATABASE'])
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = os.getenv('SUPERSET_SECRET_KEY','')
DATA_DIR = '/var/lib/superset'
LOG_LEVEL = 'INFO'
FEATURE_FLAGS = {
    'ENABLE_TEMPLATE_PROCESSING': True,
    # Uncomment this when Superset 1.3.0 upgrade is done
    # 'DASHBOARD_RBAC': True
}

AUTH_TYPE = AUTH_LDAP
AUTH_LDAP_SERVER = 'ldaps://ldap.corp.redhat.com'
AUTH_LDAP_USERNAME_FORMAT = 'uid=%s,ou=Users,dc=redhat,dc=com'
AUTH_LDAP_SEARCH = 'dc=redhat,dc=com'
AUTH_LDAP_ALLOW_SELF_SIGNED = True
AUTH_USER_REGISTRATION_ROLE = 'Datahub'
AUTH_USER_REGISTRATION = True
AUTH_LDAP_USE_TLS = False
AUTH_ROLE_ADMIN = 'Admin'
PUBLIC_ROLE_LIKE = 'Gamma'
AUTH_ROLES_MAPPING = {
    'cn=data-hub-openshift-admins,ou=adhoc,ou=managedGroups,dc=redhat,dc=com': ['Admin'],
    'cn=mhicks-all,ou=adhoc,ou=managedGroups,dc=redhat,dc=com': ['CCX'],
    'cn=ccx-dev,ou=adhoc,ou=managedGroups,dc=redhat,dc=com': ['CCX Sensitive'],
    'cn=candlepin-posix,ou=Groups,dc=redhat,dc=com': ['Subscriptions'],
    'cn=ceeandpe,ou=Groups,dc=redhat,dc=com': ['Subscriptions', 'CCX Sensitive'],
    'cn=telemeter-auth,ou=adhoc,ou=managedGroups,dc=redhat,dc=com': ['Telemetry'],
    'cn=telemeter-auto-approval,ou=adhoc,ou=managedGroups,dc=redhat,dc=com': ['Telemetry'],
    'cn=telemeter-manual-approval,ou=adhoc,ou=managedGroups,dc=redhat,dc=com': ['Telemetry']
}

# the LDAP user attribute which has their role DNs
AUTH_LDAP_GROUP_FIELD= 'memberOf'

# if we should replace ALL the user's roles each login
AUTH_ROLES_SYNC_AT_LOGIN = True

# force users to re-auth after 6 hours of inactivity (to keep roles in sync)
PERMANENT_SESSION_LIFETIME = 21600

SQLALCHEMY_ENGINE_OPTIONS = {
    'pool_size': 15,
    'pool_timeout': 60,
    'pool_recycle': 3600
}

# Set Webserver timeout to 30 minutes to wait for the queries to be executed
SUPERSET_WEBSERVER_TIMEOUT=1800
