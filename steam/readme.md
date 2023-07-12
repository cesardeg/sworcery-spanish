These steps outline the process to modify translations and generate new files to apply them in the Steam video game:

1. Copy the `base` folder and navigate to it.
   - This will serve as the working directory for the modification process.

2. Run `extract.bat` to generate the `locales` and `fonts` folders.
   - This script will extract the necessary files for translations.

3. Make necessary edits to the fonts and translations within the folder.
   - Modify the fonts and translations as needed to suit your requirements.

4. Execute `patch.bat` to build a new `sworcery.dat` and `sworcery.dat.cat`.
   - This patch file will compile the modified fonts and translations into updated game data files.

5. Copy `sworcery.dat` and `sworcery.dat.cat` to the respective folder on your system:
   - For Windows: Copy to `C:\Program Files (x86)\Steam\steamapps\common\Superbrothers Sword & Sworcery EP\res`
   - For Mac/Linux: Copy to `/home/[user]/.local/share/Steam/SteamApps/common/Superbrothers Sword & Sworcery EP/res/`

By following these steps, you can modify the translations and generate new files to apply them within the Superbrothers Sword & Sworcery EP game on Steam.
