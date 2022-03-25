#!/bin/sh
# wait-for-postgres.sh

set -e
  
host="$1"
shift
  
sleep 15
  
>&2 echo "Postgres is up - executing command"
exec "$@"