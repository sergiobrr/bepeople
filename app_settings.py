import os
from people.app.schemas import *

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = os.environ.get('SECRET_KEY') or 'uf^35kk6mvn*&b@@t*9$crigf1z(x)r00*#yd-pf)jw3ias9j0'

# ATTENZIONE SOLO IN DEVELOP...
X_DOMAINS = ['*']
X_HEADERS = ['Authorization', 'Content-Type', 'If-Match']
DEBUG = True

# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = 'primodesiderio'

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

people = {
    'item_title': 'Persons registered on primodesiderio.com',
    'schema': PeopleSchema
}

desire = {
    'item_title': 'Desires desired on primodesiderio.com',
    'schema': DesireSchema
}

# errors can only be added and retrieved: GET, POST
error = {
    'item_title': 'Vue app errors',
    'schema': ErrorSchema,
    'resource_methods': ['GET', 'POST'],
    'item_methods': ['GET']
}

URL_PREFIX = 'api/v1'
DOMAIN = {
    'people': people,
    'desire': desire,
    'error': error
}
