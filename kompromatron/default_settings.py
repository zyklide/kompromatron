import os

DEBUG = True
ASSETS_DEBUG = True

GRANO_HOST = os.environ.get('GRANO_HOST', 'http://beta.grano.cc/')
GRANO_APIKEY = os.environ.get('GRANO_APIKEY')
GRANO_PROJECT = os.environ.get('GRANO_PROJECT', 'kompromatron')

FREEZER_DESTINATION = '../build'
FREEZER_REMOVE_EXTRA_FILES = True
