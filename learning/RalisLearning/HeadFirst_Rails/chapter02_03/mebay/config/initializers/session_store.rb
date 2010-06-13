# Be sure to restart your server when you modify this file.

# Your secret key for verifying cookie session data integrity.
# If you change this key, all old sessions will become invalid!
# Make sure the secret is at least 30 characters and all random, 
# no regular words or you'll be exposed to dictionary attacks.
ActionController::Base.session = {
  :key         => '_mebay_session',
  :secret      => 'c2dff50bab18785ef44306c43ad5738ad6a8eb0e0475e27490983e4598c52f2405db4f1fd7a69504b92a9a7f08110d8c998ca702310e2437106c8b875f117963'
}

# Use the database for sessions instead of the cookie-based default,
# which shouldn't be used to store highly confidential information
# (create the session table with "rake db:sessions:create")
# ActionController::Base.session_store = :active_record_store
