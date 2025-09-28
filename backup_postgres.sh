#!/usr/bin/env bash
SCRIPT_DIRECTORY="$(dirname "$BASH_SOURCE")"
mkdir -p "${SCRIPT_DIRECTORY}/backup"
docker compose -f "${SCRIPT_DIRECTORY}/docker-compose.yml" exec db pg_dumpall>"${SCRIPT_DIRECTORY}/backup/postgres.sql"