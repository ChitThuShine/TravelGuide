import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#Definition des variables d'environnement de CleverCloud
os.environ["POSTGRESQL_ADDON_URI"] = "postgresql://u82s2ykf5m8n7zpgowkr:Pos9IfI81mKxGVQCc3LJ@bxv8u8gvxbrvggi-postgresql.services.clever-cloud.com:5432/bxv8u8gvxbrvggi"
os.environ["POSTGRESQL_ADDON_PORT"] = "5432"
os.environ["POSTGRESQL_ADDON_HOST"] = "bxv8u8gvxbrvggi-postgresql.services.clever-cloud.com"
os.environ["POSTGRESQL_ADDON_DB"] = "bxv8u8gvxbrvggi"
os.environ["POSTGRESQL_ADDON_PASSWORD"] = "votrepassword" # Votre mot de passe
os.environ["POSTGRESQL_ADDON_USER"] = "u82s2ykf5m8n7zpgowkr" # Votre nom d'utilisateur
os.environ["APP_HOME"] = BASE_DIR
os.environ["VIRTUAL_HOST"] = "http://localhost:8000"
#Injection par CleverCloud
POSTGRESQL_ADDON_URI = os.getenv("POSTGRESQL_ADDON_URI")
POSTGRESQL_ADDON_PORT = os.getenv("POSTGRESQL_ADDON_PORT ")
POSTGRESQL_ADDON_HOST = os.getenv("POSTGRESQL_ADDON_HOST")
POSTGRESQL_ADDON_DB = os.getenv("POSTGRESQL_ADDON_DB")
POSTGRESQL_ADDON_PASSWORD = os.getenv("POSTGRESQL_ADDON_PASSWORD")
POSTGRESQL_ADDON_USER = os.getenv("POSTGRESQL_ADDON_USER")
MEDIA_URL = 'storage/'
REDIS_BROKER='redis://localhost:6379'
#Vos chemins d'acces locaux sur votre machine

MEDIA_ROOT = os.getenv('APP_HOME')+'/static/storage/'
STATIC_ROOT = os.getenv('APP_HOME')+'/static/static/'
DEBUG = True