from os import getcwd
MYSITE_BASE_DIR = getcwd()

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SUPER_USER_NAME = 'admin'
SUPER_USER_EMAIL = 'admin@test.com'
SUPER_USER_PASSWORD = 'admin'

SITE_URL = '127.0.0.1:8000'
SITE_NAME = 'MySite'

DATABASE_ENGINE = 'sqlite3'    # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'mysite.db'    # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

EMAIL_HOST = 'localhost'
# EMAIL_PORT =
# EMAIL_HOST_USER =
# EMAIL_HOST_PASSWORD =