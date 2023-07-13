#!/usr/bin/env python3

import sys
import plistlib

# Get the path to the Info.plist file from the command line argument
info_plist_path = sys.argv[1]

# Open the Info.plist file
with open(info_plist_path, "rb") as fp:
    plist = plistlib.load(fp)

# Add or modify the required keys
plist["UISupportedInterfaceOrientations"] = ["UIInterfaceOrientationPortrait"]
plist["UISupportedInterfaceOrientations~ipad"] = ["UIInterfaceOrientationPortrait"]

# Save the modified Info.plist file
with open(info_plist_path, "wb") as fp:
    plistlib.dump(plist, fp)
