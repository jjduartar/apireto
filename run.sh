#!/bin/bash

# Stop & Delete container if exists
docker stop curso_api || true && docker rm _____ || true

# Run container application
docker run -itd --name curso_api -p 3000:3000 --restart always --env-file /home/rogermz/wssiscom.env rogermz/_____:1.0
