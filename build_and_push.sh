#!/bin/bash
source ./.env
set -e +u
set -o pipefail

TAG=${TAG:-"v0.1.0"}
IMG="lidofinance/deposit-cli"
export DOCKER_CONFIG=$HOME/.lidofinance

if [ -d .git ]
then
  TAG=$(git tag --points-at HEAD)
fi

echo "Building $IMG:$TAG Docker image..."
docker build -t $IMG:$TAG .

echo "Pushing $IMG:$TAG to the Docker Hub"
docker push $IMG:$TAG
docker tag $IMG:$TAG $IMG:latest
docker push $IMG:latest
