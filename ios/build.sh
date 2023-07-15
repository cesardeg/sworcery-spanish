# Get the directory of the script
script_dir=$(dirname "$(realpath "$0")")

# Validate the number of arguments
if [ $# -lt 1 ]; then
  echo "Usage: $0 <ipa_path> [locale]"
  exit 1
fi

# Get the locale from the second argument
locale=${2:-"es"}

source "${script_dir}/../utils/validate_locale.sh"
validate_locale "$locale"

# Get the IPA file path or directory
ipa_path=$1

# Validate if it's a directory
if [ -d "$ipa_path" ]; then
  # Find all IPA files in the directory
  ipa_files=($(find "$ipa_path" -type f -name "*.ipa"))
else
  # Use the specified IPA file
  ipa_files=("$ipa_path")
fi

# Validate if any IPA files are found
if [ ${#ipa_files[@]} -eq 0 ]; then
  echo "No IPA files found in the specified path."
  exit 1
fi

# Define the resource directory (res_dir)
res_dir="${script_dir}/../build/ios/${locale}"

# Create the resource directory if it doesn't exist
mkdir -p "$res_dir"

# Process each IPA file
for ipa_file in "${ipa_files[@]}"; do
  # Create a temporary directory to unzip the IPA file
  temp_dir=$(mktemp -d)
  
  # Unzip the IPA file to the temporary directory
  unzip -q "$ipa_file" -d "$temp_dir"

  # Find the .app folder inside the Payload directory
  app_folder=$(find "$temp_dir" -type d -name "*.app" -print -quit)

  if [ -z "$app_folder" ]; then
    echo "No .app folder found inside the IPA file. Skipping IPA file: $ipa_file"
    continue
  fi

  # Run the copy_files.sh script
  "${script_dir}/../utils/copy_files.sh" "$app_folder" "$locale" "mobile"

  # Modify the Info.plist using Python and plistlib
  python3 "$script_dir/patch_info_plist.py" "$app_folder/Info.plist"
  
  # Zip the modified contents back into an IPA file
  ipa_filename=$(basename "$ipa_file")
  modified_ipa="${ipa_filename%.*}-${locale}.ipa"
  (cd "$temp_dir" && zip -qr "$modified_ipa" ./*)
  
  # Move the modified IPA file to the res_dir
  mkdir -p "$res_dir"
  mv "$temp_dir/$modified_ipa" "$res_dir"
  
  # Delete the temporary directory
  rm -rf "$temp_dir"
done

echo "Modification of IPA files completed successfully!"
