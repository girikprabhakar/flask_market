#!/bin/bash

docker-compose down -v
docker image prune -a -f
