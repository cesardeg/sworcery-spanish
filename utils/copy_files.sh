#!/bin/bash

# Get the directory of the script
script_dir=$(dirname "$(realpath "$0")")

# Set the destination_dir argument to script_dir if not provided
destination_dir=$1

# Set the locale argument to "es" if not provided
locale=${2:-"es"}

# Source the validate_locale.sh script
source "${script_dir}/validate_locale.sh"

# Validate the locale
locale_name=$(validate_locale "$locale")


# Choose the appropriate files.txt based on the locale
if [[ "$locale" == "ru" ]]; then
  files_txt="${script_dir}/cyrillic_files.txt"
else
  files_txt="${script_dir}/latin_files.txt"
fi

# Determine the fonts and locales folders based on the locale
locales_folder="${script_dir}/../locales/${locale_name}"

if [[ $locale == "ru" ]]; then
  fonts_folder="${script_dir}/../fonts/cyrillic"
else
  fonts_folder="${script_dir}/../fonts/patched"
fi

# Iterate over the files in files.txt
while IFS= read -r file; do
  if [ -z "$file" ]; then
    # File path is empty, skip this iteration
    continue
  fi

  # Remove the base path (fonts/ or locales/) from the file path
  file_path="${file#fonts/}"
  file_path="${file_path#locales/}"

  # Construct the source and destination paths
  destination_path="${destination_dir}/${file}"

  if [[ $file == fonts/* ]]; then
    source_path="${fonts_folder}/${file_path}"
  elif [[ $file == locales/* ]]; then
    source_path="${locales_folder}/${file_path}"
  fi

  # Skip the file if the source path doesn't exist
  if [[ ! -e "$source_path" ]]; then
    echo "Source path does not exist: $source_path. Skipping..."
    continue
  fi

  # Create the destination directory if it doesn't exist
  destination_file_dir=$(dirname "${destination_path}")
  mkdir -p "${destination_file_dir}"

  # Copy the file to the destination directory
  cp -f "${source_path}" "${destination_path}"

done < "$files_txt"
