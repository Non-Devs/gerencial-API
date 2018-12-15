#!/usr/bin/env bash
set -o errexit -o nounset

# Configure the git inside of Travis Machine
(
  git config user.name "${GH_USER_NAME}"
  git config user.email "${GH_USER_EMAIL}"
)

# Running mkdocs build to gh-pages
docker-compose run --rm web bash -c "mkdocs gh-deploy"