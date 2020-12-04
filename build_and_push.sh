#!/bin/bash
source ./.env
set -e +u
set -o pipefail
TAG="v1.1.0-lido.2"
IMG="lidofinance/deposit-cli"
export DOCKER_CONFIG=$HOME/.lidofinance

echo "Building oracle Docker image..."
docker build -t "$IMG:$TAG" .

echo "Pushing image to the Docker Hub"
docker push "$IMG:$TAG"
docker tag "$IMG:$TAG" "$IMG:latest"
