#!/bin/bash

# Get the directory of the script
script_dir=$(dirname "$(realpath "$0")")

# Set the res_dir argument to script_dir if not provided
res_dir=${1:-"$script_dir"}

# Update the sworcery.dat file using 7za

(cd "${res_dir}" && 7za u sworcery.dat @"${script_dir}/files.txt" -pGdHGhd4yuNF)
