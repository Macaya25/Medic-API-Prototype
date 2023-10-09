#!/usr/bin/env bash

#!/usr/bin/env bash

TRY_LOOP="20"

: "${POSTGRES_HOST:="postgres"}"
: "${POSTGRES_PORT:="5432"}"

wait_for_port() {
  local name="$1" host="$2" port="$3"
  local j=0
  while ! nc -z "$host" "$port" >/dev/null 2>&1 < /dev/null; do
    j=$((j+1))
    if [ $j -ge $TRY_LOOP ]; then
      echo >&2 "$(date) - $host:$port still not reachable, giving up"
      exit 1
    fi
    echo "$(date) - waiting for $name... $j/$TRY_LOOP"
    sleep 5
  done
}

echo "$POSTGRES_HOST" "$POSTGRES_PORT"
wait_for_port "Postgres" "$POSTGRES_HOST" "$POSTGRES_PORT"

echo "starting api"

alembic upgrade head
uvicorn main:app --reload --port=$SERVICE_PORT --host=0.0.0.0
