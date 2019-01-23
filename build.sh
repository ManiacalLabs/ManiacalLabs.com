#!/bin/bash

set -o xtrace

if [[ "$TRAVIS_PULL_REQUEST_BRANCH" || $TRAVIS_BRANCH != 'master' ]]; then
  echo "Modifying for stage deploy"
  sed -i 's/ManiacalLabs.com/stage.ManiacalLabs.com/g' $TRAVIS_BUILD_DIR/config.yaml
fi

chmod +x $TRAVIS_BUILD_DIR/bin/hugo
$TRAVIS_BUILD_DIR/bin/hugo

if [[ "$TRAVIS_PULL_REQUEST_BRANCH" || $TRAVIS_BRANCH != 'master' ]]; then
  echo "Syncing to stage server"
  rsync -rav --delete $TRAVIS_BUILD_DIR/public/ cyrberus@stage.maniacallabs.com:/home/cyrberus/stage.maniacallabs.com/
fi
