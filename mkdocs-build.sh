#!/usr/bin/env bash
set -o errexit -o nounset

# Get current commit revision
rev=$(git rev-parse --short HEAD)

# Configure the git inside of Travis Machine
(
  git config user.name "${GH_USER_NAME}"
  git config user.email "${GH_USER_EMAIL}"
  git remote remove origin
  git remote add origin "https://${GH_TOKEN}@github.com/Non-Devs/gerencial-API.git"
  git fetch origin
)

# Running mkdocs build to gh-pages
mkdocs build --clean