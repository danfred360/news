#!/bin/bash
set -e

# Perform all actions as $POSTGRES_USER
export PGUSER="$POSTGRES_USER"

# echo "creating news database"
# # Create the news database
# "${psql[@]}" --dbname="$POSTGRES_DB" <<-EOSQL
#     CREATE DATABASE news;
# EOSQL

echo "running sql init files"
# run sql init files
echo "loading extensions..."
"${psql[@]}" --dbname="news" -f /sqlscripts/load_extensions.sql
echo "creating tables..."
"${psql[@]}" --dbname="news" -f /sqlscripts/create_tables.sql

echo "tables in news -->"
"${psql[@]}" --dbname="news" <<-EOSQL 
    \dt; 
EOSQL

echo "seeding data..."
"${psql[@]}" --dbname="news" -f /sqlscripts/seed.sql

echo "enable logging..."
"${psql[@]}" --dbname="news" -c "ALTER SYSTEM SET logging_collector = 'on';"
"${psql[@]}" --dbname="news" -c "ALTER SYSTEM SET log_destination = 'stderr';"
"${psql[@]}" --dbname="news" -c "ALTER SYSTEM SET log_directory = '/var/log/postgresql';"
"${psql[@]}" --dbname="news" -c "SELECT pg_reload_conf();"