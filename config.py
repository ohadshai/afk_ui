import os
from flask_appbuilder.security.manager import (
    AUTH_OID,
    AUTH_REMOTE_USER,
    AUTH_DB,
    AUTH_LDAP,
    AUTH_OAUTH,
)

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # Your App secret key
    SECRET_KEY = "\2\1thisismyscretkey\1\2\e\y\y\h"

    # Flask-WTF flag for CSRF
    CSRF_ENABLED = True

    # ------------------------------
    # GLOBALS FOR APP Builder
    # ------------------------------

    # Uncomment to setup Setup an App icon
    # APP_ICON = "static/img/logo.jpg"

    # ----------------------------------------------------
    # AUTHENTICATION CONFIG
    # ----------------------------------------------------
    # The authentication type
    # AUTH_OID : Is for OpenID
    # AUTH_DB : Is for database (username/password()
    # AUTH_LDAP : Is for LDAP
    # AUTH_REMOTE_USER : Is for using REMOTE_USER from web server
    AUTH_TYPE = AUTH_DB

    # Uncomment to setup Full admin role name
    # AUTH_ROLE_ADMIN = 'Admin'

    # Uncomment to setup Public role name, no authentication needed
    # AUTH_ROLE_PUBLIC = 'Public'

    # Will allow user self registration
    # AUTH_USER_REGISTRATION = True

    # The default user self registration role
    # AUTH_USER_REGISTRATION_ROLE = "Public"

    # When using LDAP Auth, setup the ldap server
    # AUTH_LDAP_SERVER = "ldap://ldapserver.new"

    # Uncomment to setup OpenID providers example for OpenID authentication
    # OPENID_PROVIDERS = [
    #    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    #    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    #    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    #    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]
    # ---------------------------------------------------
    # Babel config for translations
    # ---------------------------------------------------
    # Setup default language
    BABEL_DEFAULT_LOCALE = "en"
    # Your application default translation path
    BABEL_DEFAULT_FOLDER = "translations"
    # The allowed translation for you afk_ui
    LANGUAGES = {
        "en": {"flag": "gb", "name": "English"},
        "pt": {"flag": "pt", "name": "Portuguese"},
        "pt_BR": {"flag": "br", "name": "Pt Brazil"},
        "es": {"flag": "es", "name": "Spanish"},
        "de": {"flag": "de", "name": "German"},
        "zh": {"flag": "cn", "name": "Chinese"},
        "ru": {"flag": "ru", "name": "Russian"},
        "pl": {"flag": "pl", "name": "Polish"},
    }
    # ---------------------------------------------------
    # Image and file configuration
    # ---------------------------------------------------
    # The file upload folder, when using models with files
    UPLOAD_FOLDER = basedir + "/afk_ui/static/uploads/"

    # The image upload folder, when using models with images
    IMG_UPLOAD_FOLDER = basedir + "/afk_ui/static/uploads/"

    # The image upload url, when using models with images
    IMG_UPLOAD_URL = "/static/uploads/"
    # Setup image size default is (300, 200, True)
    # IMG_SIZE = (300, 200, True)

    # Theme configuration
    # these are located on static/appbuilder/css/themes
    # you can create your own and easily use them placing them on the same dir structure to override
    # APP_THEME = "bootstrap-theme.css"  # default bootstrap
    # APP_THEME = "cerulean.css"
    # APP_THEME = "amelia.css"
    # APP_THEME = "cosmo.css"
    # APP_THEME = "cyborg.css"
    # APP_THEME = "flatly.css"
    # APP_THEME = "journal.css"
    #APP_THEME = "readable.css"
    # APP_THEME = "simplex.css"
    # APP_THEME = "slate.css"
    # APP_THEME = "spacelab.css"
    # APP_THEME = "united.css"
    # APP_THEME = "yeti.css"

    APP_NAME = "AFK"
    # APP_ICON = "static/img/Apple-Logo-Hack.jpg"
    FAB_API_SWAGGER_UI = True
    SQLALCHEMY_TRACK_MODIFICATIONS = FAB_API_SWAGGER_UI
    DEBUG = False
    TESTING = False


    SQLALCHEMY_DATABASE_URI = "jdbc:mariadb://60.150.1.XXX:3306/DB?user=root&password=myPassword"
    #########################################################################
    # SQLALCHEMY_DATABASE_URI = 'mysql://myapp@localhost/myapp'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://root:password@localhost/myapp'

    JENKINS_URI = "http://localhost:8080"
    ELK_URI = "http://localhost:9200"
    ELASTIC_APM = {
        "SERVICE_NAME": "UfkApp",
        "SECRET_TOKEN": "",
        "SERVICE_URL": "http://localhost:8200",
        'FLUSH_INTERVAL': 1,
        'MAX_QUEUE_SIZE': 1,
        "DEBUG": True
    }
    DSM_PAGE_SIZE = 3


class ProductionConfig(Config):
    '''All necessary Production configuration'''
    DSM_SERVER = "http://afk-server:8081"

class DevelopmentConfig(Config):
    '''All necessary Development configuration'''
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db")
    DSM_SERVER = "http://afk-dev-server:8081"
    DEBUG = True


class TestingConfig(Config):
    '''All necessary Testing configuration'''
    TESTING = True
