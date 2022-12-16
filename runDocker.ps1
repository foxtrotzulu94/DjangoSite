#!/bin/bash
docker kill personal_site
docker rm personal_site
docker build -t personal_site . --build-arg ENV_DEBUG=1
docker run -p8000:7654 -v ${PSScriptRoot}/static:/app/static -v ${PSScriptRoot}/media:/app/media -v ${PSScriptRoot}/db.sqlite3:/app/db.sqlite3 --name personal_site personal_site
