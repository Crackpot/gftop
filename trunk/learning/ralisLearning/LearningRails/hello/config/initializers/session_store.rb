# Be sure to restart your server when you modify this file.

# Your secret key for verifying cookie session data integrity.
# If you change this key, all old sessions will become invalid!
# Make sure the secret is at least 30 characters and all random, 
# no regular words or you'll be exposed to dictionary attacks.
ActionController::Base.session = {
  :key         => '_hello_session',
  :secret      => 'cffca471910f84d58819062172aa5c4407e1d0083ba49c720d21114ec3a9215bb0a024fd18e9a3ea5f27910918696c39adc1d095786c3b5230685bb9645a9c9e'
}

# Use the database for sessions instead of the cookie-based default,
# which shouldn't be used to store highly confidential information
# (create the session table with "rake db:sessions:create")
# ActionController::Base.session_store = :active_record_store
