# IPA Modification Scripts

This project provides a set of scripts to modify IPA (iOS App Store Package) files. The scripts allow for patching the font, locale, and Info.plist files of an IPA, enabling you to generate modified IPAs with specific translations and fixes. This can be particularly useful for customizing and localizing iOS apps.

## Requirements

- Python 3.x
- `unzip` command-line tool
- OpenSSH (for `scp.sh` script)
- Jailbroken iPhone with OpenSSH (for `scp.sh` script)

## Getting Started

1. Clone the repository to your local machine:

```shell
git clone https://github.com/cesardeg/swordable.git
cd ios
```

2. Ensure that you have the necessary requirements installed, as mentioned in the Requirements section.

## Scripts

### build.sh

This script allows you to modify IPA files by patching the font, locale, and Info.plist files. It supports batch processing of multiple IPAs.

#### Usage:

```shell
./build.sh <ipa_path> [locale]
```

- `<ipa_path>`: The path to the IPA file or directory containing multiple IPAs.
- `[locale]` (optional): The desired locale ["es", "pt"]. Default is "es" (Spanish).

The modified IPAs will be saved in the `/build/ios` directory.

### patch_info_plist.py

This Python script is used to patch the Info.plist file of an IPA. It resolves a bug in iOS 16+ where the game is not playable due to the game rendering only in portrait mode.

#### Usage:

```shell
python patch_info_plist.py <info_plist_path>
```

- `<info_plist_path>`: The path to the Info.plist file.

### scp.sh

This script allows you to copy translation files to an iPhone with jailbreak and OpenSSH using SCP (Secure Copy). It connects to the iPhone and copies the necessary files to the appropriate directories.

#### Usage:

```shell
./scp.sh <remote_ip> [locale]
```

- `<remote_ip>`: The IP address of the remote iPhone.
- `[locale]` (optional): The desired locale. Default is "es" (Spanish).

Please note that you need to have the necessary permissions and setups in place for OpenSSH and Jailbroken iPhone with OpenSSH in order to use the `scp.sh` script.

