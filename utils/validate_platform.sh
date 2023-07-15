#!/bin/bash

# Validate if the platform is supported
function validate_platform {
  platform=$1

  if [ "$platform" != "desk" ] && [ "$platform" != "mobile" ]; then
    echo "Invalid platform. Valid platforms are: desk, mobile"
    exit 1
  fi
}
