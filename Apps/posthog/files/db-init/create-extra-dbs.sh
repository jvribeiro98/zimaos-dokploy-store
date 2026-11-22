#!/bin/bash
# Creates the auxiliary databases PostHog services can point at
# (mirrors docker/postgres-init-scripts in the PostHog repo)
set -e
set -u

for db in cyclotron posthog_persons behavioral_cohorts; do
    DB_EXISTS=$(psql -U "$POSTGRES_USER" -tAc "SELECT 1 FROM pg_database WHERE datname='$db'")
    if [ -z "$DB_EXISTS" ]; then
        echo "Creating database '$db'..."
        psql -U "$POSTGRES_USER" -c "CREATE DATABASE $db;"
        psql -U "$POSTGRES_USER" -c "GRANT ALL PRIVILEGES ON DATABASE $db TO $POSTGRES_USER;"
    fi
done
