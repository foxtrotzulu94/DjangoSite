#!/bin/bash
docker kill personal_site
docker rm personal_site
docker build -t personal_site .
docker run -p8000:8000 --name personal_site personal_site
