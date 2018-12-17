#!/usr/bin/env bash
set -o errexit

rm -rf public
mkdir public

# config
git config --global user.email "${GH_USER_EMAIL}"
git config --global user.name "${GH_USER_NAME}"

# build (CHANGE THIS)
mkdocs build --clean

# deploy
cd public
git init
git add .
git commit -m "Deploy to Github Pages"
git push --force --quiet "https://${GH_TOKEN}@github.com/Non-Devs/gerencial-API.git" develop:gh-pages > /dev/null 2>&1