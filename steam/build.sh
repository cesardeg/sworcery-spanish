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

locale_dir=""
case "$locale" in
  "es") locale_dir="spanish";;
  "pt") locale_dir="portuguese";;
  *) echo "Invalid locale. Valid locales are: es, pt"; exit 1;;
esac

# Set the res dir based on the script directory and locale
res_dir="${script_dir}/../build/steam/$locale_dir"

# Create the res directory if it doesn't exist
mkdir -p "$res_dir"

# Copy the sworcery.dat file to the res directory
cp "$sworcery_dat_path" "$res_dir"

# Run the unpack.sh script
"${script_dir}/unpack.sh" "$res_dir"

# Copy files from locales/${locale_dir}/ to build/locales
locales_files=$(grep -E '^locales/' "${script_dir}/files.txt" | sed 's/^locales\///')
while IFS= read -r file; do
  cp "${script_dir}/../locales/${locale_dir}/$file" "${res_dir}/locales/"
done <<< "$locales_files"

# Copy files from fonts/patched/ to build/fonts
fonts_files=$(grep -E '^fonts/' "${script_dir}/files.txt" | sed 's/^fonts\///')
while IFS= read -r file; do
  cp "${script_dir}/../fonts/patched/$file" "${res_dir}/fonts/"
done <<< "$fonts_files"

# Run the repack.sh script
"${script_dir}/repack.sh" "$res_dir"

# Run the build-cat.py script
"${script_dir}/build-cat.py" "$res_dir"

echo "Localization build completed for locale: $locale"
