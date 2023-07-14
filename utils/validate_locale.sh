#!/bin/bash

# Validate if the locale is supported
function validate_locale {
  local locale=$1
  local name

  case "$locale" in
    "es") name="spanish";;
    "fr") name="french";;
    "it") name="italian";;
    "pt") name="portuguese";;
    "ru") name="russian";;
    *) echo "Invalid locale. Valid locales are: es, fr, it, pt, ru"; exit 1;;
  esac

  echo "$name"
}
