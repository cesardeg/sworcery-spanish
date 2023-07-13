#!/usr/bin/env python3

import paramiko
import os
import sys

script_name = os.path.basename(sys.argv[0])

# Validate the number of arguments
if len(sys.argv) < 2:
    print(f"Usage: {script_name} <ip> [locale]")
    exit(1)

# SSH server configuration
ip_address = sys.argv[1]
port = 22
username = 'root'
password = 'alpine'

# Script directory
script_dir = os.path.dirname(os.path.realpath(__file__))

# Local file paths for fonts and locales
fonts_dir = os.path.join(script_dir, "..", "fonts", "patched")
locales_dir = os.path.join(script_dir, "..", "locales")

# Destination paths on the iPhone for fonts and locales
fonts_dest = "/var/containers/Bundle/Application/{uuid}/SwordAndSworcery-Uni.app/fonts/"
locales_dest = "/var/containers/Bundle/Application/{uuid}/SwordAndSworcery-Uni.app/locales/"

# Get the language_dir based on the locale
locale = sys.argv[2] if len(sys.argv) >= 3 else "es"
language_dir = ""
if locale == "es":
    language_dir = "spanish"
elif locale == "pt":
    language_dir = "portuguese"
else:
    print("Invalid locale. Valid locales are: es, pt")
    exit(1)

# Create an SSH client instance
client = paramiko.SSHClient()
client.load_system_host_keys()

try:
    # Add the server's host key to the known hosts file
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the SSH server
    client.connect(ip_address, port, username, password)

    # Create an SFTP client
    sftp = client.open_sftp()

    # Find the app folder that contains SwordAndSworcery-Uni.app
    app_folder_path = None
    app_folders = sftp.listdir("/var/containers/Bundle/Application")
    for folder in app_folders:
        app_path = f"/var/containers/Bundle/Application/{folder}/SwordAndSworcery-Uni.app"
        try:
            sftp.stat(app_path)
            app_folder_path = folder
            break
        except FileNotFoundError:
            pass

    if not app_folder_path:
        print("No SwordAndSworcery-Uni.app folder found in /var/containers/Bundle/Application")
        exit(1)

    # Copy font files to the iPhone
    for file in ["conduit_itc.fnt", "conduit_itc_2x.fnt", "conduit_itc_4x.fnt"]:
        local_file_path = os.path.join(fonts_dir, file)
        remote_file_path = fonts_dest.format(uuid=app_folder_path) + file
        sftp.put(local_file_path, remote_file_path)
        print(f"Successful copy: {file}")

    # Copy locale files to the iPhone
    for file in ["strings.tsv", "dialog.tsv"]:
        local_file_path = os.path.join(locales_dir, language_dir, file)
        remote_file_path = locales_dest.format(uuid=app_folder_path) + file
        sftp.put(local_file_path, remote_file_path)
        print(f"Successful copy: {file}")

    print("File copying completed.")

finally:
    # Close the SFTP and SSH client connections
    if sftp:
        sftp.close()
    if client:
        client.close()
