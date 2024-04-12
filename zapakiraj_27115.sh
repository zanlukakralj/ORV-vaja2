#!/bin/bash

# Zgradi Docker image
docker build -t zanlukakralj/orv-vaja2 .

# Potisni image na DockerHub
docker push zanlukakralj/orv-vaja2
