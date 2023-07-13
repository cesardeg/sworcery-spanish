#!/bin/bash

# Get the directory of the script
script_dir=$(dirname "$(realpath "$0")")

# Set the res_dir argument to script_dir if not provided
res_dir=${1:-"$script_dir"}

# Extract files using 7za
7za x -aoa "${res_dir}/sworcery.dat" -i@"${script_dir}/files.txt" -o"${res_dir}" -pGdHGhd4yuNF
