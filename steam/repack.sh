#!/bin/bash

# Get the directory of the script
script_dir=$(dirname "$(realpath "$0")")

# Set the res_dir argument to script_dir if not provided
res_dir=${1:-"$script_dir"}

locale=$2

if [[ "$locale" == "ru" ]]; then
  files_txt="${script_dir}/../utils/files/desk_cyrillic.txt"
else
  files_txt="${script_dir}/../utils/files/desk_latin.txt"
fi

# Update the sworcery.dat file using 7za
(cd "${res_dir}" && 7za u sworcery.dat @"${files_txt}" -pGdHGhd4yuNF)
