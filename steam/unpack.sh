#!/bin/bash

# Get the directory of the script
script_dir=$(dirname "$(realpath "$0")")

# Set the res_dir argument to script_dir if not provided
res_dir=${1:-"$script_dir"}

# Loop through the files listed in files.txt and extract them
while IFS= read -r file; do
  unzip -P GdHGhd4yuNF -o "${res_dir}/sworcery.dat" "$file" -d "${res_dir}"
done < "${script_dir}/files.txt"

