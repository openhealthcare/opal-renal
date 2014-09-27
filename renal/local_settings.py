DEBUG=True
# DATABASES= {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'USER': 'ohc',
#         'PASSWORD': 'wombles',
#         'HOST': 'localhost',
#         'NAME': 'elcidutf8'
#     }
# }

OPAL_LOG_OUT_DURATION = 1 * 60 * 1000
OPAL_LOG_OUT_DURATION = 100 * 60 * 1000


# , edit settings.py. It's a normal Python module with module-level variables representing Django settings. Change the following keys in the DATABASES 'default' item to match your databases connection settings.

# ENGINE -- Either 'django.db.backends.postgresql_psycopg2', 'django.db.backends.mysql' or 'django.db.backends.sqlite3'. Other backends are also available.

# NAME -- The name of your database. If you're using SQLite, the database will be a file on your computer; in that case, NAME should be the full absolute path, including filename, of that file. If the file doesn't exist, it will automatically be created when you synchronize the database for the first time (see below).

# When specifying the path, always use forward slashes, even on Windows (e.g. C:/homes/user/mysite/sqlite3.db).

# USER -- Your database username (not used for SQLite).

# PASSWORD -- Your database password (not used for SQLite).

# HOST -- The host your database is on. Leave this as an empty string if your database server is on the same physical machine (not used for SQLite).
