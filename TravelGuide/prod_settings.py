"""
Django settings for  project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
import os

POSTGRESQL_ADDON_URI = os.getenv("POSTGRESQL_ADDON_URI")
POSTGRESQL_ADDON_PORT = os.getenv("POSTGRESQL_ADDON_PORT ")
POSTGRESQL_ADDON_HOST = os.getenv("POSTGRESQL_ADDON_HOST")
POSTGRESQL_ADDON_DB = os.getenv("POSTGRESQL_ADDON_DB")
POSTGRESQL_ADDON_PASSWORD = os.getenv("POSTGRESQL_ADDON_PASSWORD")
POSTGRESQL_ADDON_USER = os.getenv("POSTGRESQL_ADDON_USER")
MEDIA_URL = 'http://app-fc3dfb6c-6a65-4b24-a1ca-88dac7fcbd85.cleverapps.io/storage/'
MEDIA_ROOT = os.getenv('APP_HOME')+'/static/storage/'
STATIC_ROOT = os.getenv('APP_HOME')+'/static/static/'
REDIS_BROKER='redis://:7KDKUlbl9ebxq4JjYH9@bwscqsr7i-redis.services.clever-cloud.com:3025'
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
# To send push on production set Debug=FALSE sinon a TRUE en PREPROD
DEBUG = False

