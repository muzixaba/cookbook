# Save secrets in .env file & add it to .gitignore
# All vars are strings

# .env
# export SECRET_KEY="MyActualSecretKey"

import os

SECRET_KEY = os.environ.get('SECRET_KEY', 'ThisIsADummyKey')

# DEBUG=0 on production server
DEBUG = bool(int(os.environ.get('DEBUG', 1)))