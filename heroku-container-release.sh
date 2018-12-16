#!/bin/bash

if [ $# -ne 4 ]; then
  echo "The number of parameters is $#." 1>&2
  echo "4 parameters required." 1>&2
  echo "1 - api-prod-gerencial" 1>&2
  echo "2 - web" 1>&2
  echo "4 - HEROKU_AUTH_TOKEN" 1>&2
  exit 1
fi

readonly api-prod-gerencial=$1
readonly web=$2
readonly HEROKU_AUTH_TOKEN=$4

imageId=$(docker inspect registry.heroku.com/api-prod-gerencial/web --format={{.Id}})
payload='{"updates":[{"type":"web","docker_image":"'"$imageId"'"}]}'
curl -n -X PATCH https://api.heroku.com/apps/api-prod-gerencial/formation \
-d "$payload" \
-H "Content-Type: application/json" \
-H "Accept: application/vnd.heroku+json; version=3.docker-releases" \
-H "Authorization: Bearer $HEROKU_AUTH_TOKEN"