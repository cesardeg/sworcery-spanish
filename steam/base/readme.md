These are the steps to modify the translations and generate new files to apply them in the Steam video game. Make sure you have access to the following files for making the modifications:

1. Translation Files:
   - `locales/dialog.tsv`
   - `locales/strings.tsv`

2. Font Files:
   - `fonts/conduit_itc.fnt`
   - `fonts/conduit_itc_ipad.fnt`

Follow the steps below:

1. Create a copy of this folder and navigate to it.
   - This folder will serve as your working directory for the modification process.

2. Run `extract.bat` to generate the `locales` and `fonts` folders.
   - This script will extract the necessary files for translations.

3. Make the necessary modifications to the `dialog.tsv` and `strings.tsv` files in the `locales` folder.
   - Edit the texts and translations according to your preferences.

4. Replace `conduit_itc.fnt` and `conduit_itc_ipad.fnt` font files with the patched versions in the `fonts` folder
   - To support special characters that do not exist in English, please refer to the fonts readme for more information.

5. Run `patch.bat` to generate new `sworcery.dat` and `sworcery.dat.cat` files.
   - This batch file will compile the modified translations into updated game data files.

6. Copy the newly generated `sworcery.dat` and `sworcery.dat.cat` files to the appropriate location in your game installation directory:

   - For Windows:
     - Copy `sworcery.dat` and `sworcery.dat.cat` to:
       `C:\Program Files (x86)\Steam\steamapps\common\Superbrothers Sword & Sworcery EP\res`

   - For Linux/Mac:
     - Copy `sworcery.dat` and `sworcery.dat.cat` to:
       `/Users/[username]/Library/Application Support/Steam/SteamApps/common/Superbrothers Sword & Sworcery EP/res`

By following these steps, you will be able to modify the translations and generate new files to apply them within the Superbrothers Sword & Sworcery EP game on Steam. Feel free to edit the translation files to suit your preferences.
