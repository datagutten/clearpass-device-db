#!/usr/bin/env bash
docker compose cp ./sql/roles.sql db:/home/roles.sql
docker compose exec -i db psql -f /home/roles.sql
