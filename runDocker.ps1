#!/bin/bash
docker kill personal_site
docker rm personal_site
docker build -t personal_site . --build-arg ENV_DEBUG=1
docker run -p8000:7654 -v ${PSScriptRoot}/media:/app/media --name personal_site personal_site "python" "manage.py" "runserver" "0.0.0.0:7654"
