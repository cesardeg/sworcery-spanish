#!/bin/bash

# Get the directory of the script
script_dir=$(dirname "$(realpath "$0")")

# Set the res_dir argument to script_dir if not provided
res_dir=${1:-"$script_dir"}

# Update the sworcery.dat file using zip
(cd "${res_dir}" && zip -u -P GdHGhd4yuNF sworcery.dat -@ < "${script_dir}/files.txt")
