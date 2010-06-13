# Be sure to restart your server when you modify this file.

# Your secret key for verifying cookie session data integrity.
# If you change this key, all old sessions will become invalid!
# Make sure the secret is at least 30 characters and all random, 
# no regular words or you'll be exposed to dictionary attacks.
ActionController::Base.session = {
  :key         => '_Workout_session',
  :secret      => '59694503102387dd72259f659a88363b3e91a727f6f2ac3e77d28c68b97d719d7cdd9ded3bceca2f880b491abe27f0c12e7819f50bc4a9fab395347893db72f7'
}

# Use the database for sessions instead of the cookie-based default,
# which shouldn't be used to store highly confidential information
# (create the session table with "rake db:sessions:create")
# ActionController::Base.session_store = :active_record_store
