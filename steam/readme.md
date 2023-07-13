# Sworcery Localization Scripts

This project provides a set of scripts for generating localized files (`sworcery.dat` and `sworcery.dat.cat`) for the game "Sworcery". These files can be used to change the game's language by replacing the original files with the localized ones.

## Requirements

- Bash
- Python 3.x
- 7-Zip (command-line version)

## Getting Started

1. Clone the repository to your local machine:

```shell
git clone https://github.com/your-username/sworcery-localization.git
cd sworcery-localization
```

2. Ensure that you have the necessary requirements installed, as mentioned in the Requirements section.

## Scripts

### build.sh

This script generates the localized files (`sworcery.dat` and `sworcery.dat.cat`) for the "Sworcery" game. It supports generating files for different locales.

#### Usage:

```shell
./build.sh <sworcery_dat_path> [locale]
```

- `<sworcery_dat_path>`: The path to the original `sworcery.dat` file.
- `[locale]` (optional): The desired locale. Default is "es" (Spanish).

The localized files will be generated in the `build/steam/{locale}` directory.

### unpack.sh

This script is used to unpack the `sworcery.dat` file using 7-Zip.

#### Usage:

```shell
./unpack.sh [res_dir]
```

- `[res_dir]` (optional): The directory containing the `sworcery.dat` file. Default is the current directory.

### repack.sh

This script is used to repack the modified files into a new `sworcery.dat` file using 7-Zip.

#### Usage:

```shell
./repack.sh [res_dir]
```

- `[res_dir]` (optional): The directory containing the modified files. Default is the current directory.

### build-cat.py

This Python script generates the `sworcery.dat.cat` file, which contains information about the resource files in the `sworcery.dat` archive.

#### Usage:

```shell
python build-cat.py [folder]
```

- `[folder]` (optional): The folder containing the `sworcery.dat` and `sworcery.dat.cat` files. Default is the current directory.

## Usage

1. Run the `build.sh` script to generate the localized files. For example, to generate the files for the Spanish locale:

```shell
./build.sh /path/to/sworcery.dat es
```

2. The localized files (`sworcery.dat` and `sworcery.dat.cat`) will be generated in the `build/steam/{locale}` directory.

3. Copy the generated files to the appropriate location in the game directory to change the game's language.

Please note that the game directory structure may vary depending on the platform. Make sure to follow the game's installation instructions for your specific platform.

## Notes

- The original `sworcery.dat` file should be obtained from a legitimate source. This project only provides the scripts for generating localized files, not the original game files.
- Make sure to backup the original game files before replacing them with the localized files.
- The `build-cat.py` script is automatically called by the `build.sh` script and does not need to be run separately.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
