#!/bin/bash

if [[ $TRAVIS_BRANCH != 'master' ]]; then
  sed -i 's/ManiacalLabs.com/stage.ManiacalLabs.com/g' $TRAVIS_BUILD_DIR/config.yaml
fi

chmod +x $TRAVIS_BUILD_DIR/bin/hugo
$TRAVIS_BUILD_DIR/bin/hugo
