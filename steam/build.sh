#!/bin/bash

# Get the directory of the script
script_dir=$(dirname "$(realpath "$0")")

# Validate the number of arguments
if [ $# -lt 1 ]; then
  echo "Usage: $0 <sworcery.dat_path> [locale]"
  exit 1
fi

# Get the sworcery.dat path from the argument
sworcery_dat_path=$1

# Validate if the sworcery.dat file exists
if [ ! -f "$sworcery_dat_path" ]; then
  echo "The sworcery.dat file does not exist at the specified path: $sworcery_dat_path"
  exit 1
fi

# Set locale argument
locale=${2:-"es"}

source "${script_dir}/../utils/validate_locale.sh"
validate_locale "$locale"

# Set the res dir based on the script directory and locale
res_dir="${script_dir}/../build/steam/$locale"

# Create the res directory if it doesn't exist
mkdir -p "$res_dir"

# Copy the sworcery.dat file to the res directory
cp "$sworcery_dat_path" "$res_dir"

# Run the unpack.sh script
"${script_dir}/unpack.sh" "$res_dir"

# Run the copy_files.sh script
"${script_dir}/../utils/copy_files.sh" "$res_dir" "$locale"

# Run the repack.sh script
"${script_dir}/repack.sh" "$res_dir"

# Run the build-cat.py script
"${script_dir}/build-cat.py" "$res_dir"

echo "Localization build completed for locale: $locale"
