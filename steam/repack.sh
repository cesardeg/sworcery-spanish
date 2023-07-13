#!/bin/bash

# Get the directory of the script
script_dir=$(dirname "$(realpath "$0")")

# Set the res_dir argument to script_dir if not provided
res_dir=${1:-"$script_dir"}

# Concatenate res_dir path to each file in files.txt
files=$(sed "s#^#${res_dir}/#" "${script_dir}/files.txt")

# Update the sworcery.dat file using 7za
7za u "${res_dir}/sworcery.dat" ${files} -pGdHGhd4yuNF
