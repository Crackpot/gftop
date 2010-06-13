# Be sure to restart your server when you modify this file.

# Your secret key for verifying cookie session data integrity.
# If you change this key, all old sessions will become invalid!
# Make sure the secret is at least 30 characters and all random, 
# no regular words or you'll be exposed to dictionary attacks.
ActionController::Base.session = {
  :key         => '_coconut_session',
  :secret      => 'e694e1b7239666f1fc1198dbf53ae0ce7d9303a0a9209c72649daaca5d142112b1419c15e49799e284c5654b7f41cf0e3e10843ce79a148f481f31effd49631b'
}

# Use the database for sessions instead of the cookie-based default,
# which shouldn't be used to store highly confidential information
# (create the session table with "rake db:sessions:create")
# ActionController::Base.session_store = :active_record_store
