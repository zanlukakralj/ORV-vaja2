#!/bin/bash

# Pull Docker image from DockerHub
docker pull zanlukakralj/orv-vaja2

# Run Docker container
docker run -d -p 8080:80 zanlukakralj/orv-vaja2
