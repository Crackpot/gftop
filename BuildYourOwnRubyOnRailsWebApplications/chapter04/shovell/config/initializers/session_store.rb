# Be sure to restart your server when you modify this file.

# Your secret key for verifying cookie session data integrity.
# If you change this key, all old sessions will become invalid!
# Make sure the secret is at least 30 characters and all random, 
# no regular words or you'll be exposed to dictionary attacks.
ActionController::Base.session = {
  :key         => '_shovell_session',
  :secret      => '3b8f2cd941ea944f7820476acafb7867d80841ca4c2dfa9329342114ac411ab8d9680bc7010b3c7ecd0ef5bc721a2c2a7c35a4f31a20b6a0019450b68bef4aa1'
}

# Use the database for sessions instead of the cookie-based default,
# which shouldn't be used to store highly confidential information
# (create the session table with "rake db:sessions:create")
# ActionController::Base.session_store = :active_record_store
