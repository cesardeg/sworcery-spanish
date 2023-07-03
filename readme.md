# Game Translation to Spanish

This guide will walk you through the steps to translate the game to Spanish and fix the special character display issues.

## Translating the Game

The game translation files are located in the `locales` directory. To translate the game to Spanish, follow these steps:

1. Replace the `locales/strings.tsv` file in a text editor.
2. Find the English phrases or sentences and replace them with their corresponding Spanish translations.
3. Save the file.

Next, you need to translate the game dialogues. Here's how:

1. Open the `locales/dialog.tsv` file in a text editor.
2. Locate the English dialogues and replace them with their Spanish translations.
3. Save the file.

## Fixing Special Characters

To fix the special character display issues in the game, we will modify the fonts. The font files are located in the `fonts` directory. Follow the steps below:

1. Make a backup of the original font files in case you need to revert the changes.
2. Open a file explorer and navigate to the `fonts` directory.
3. Look for the font files starting with `conduit_itc` (e.g., `conduit_itc_regular.fnt`, `conduit_itc_bold.fnt`, etc.).
4. Replace the font files with the modified versions that support upper-case special characters.
   - The modified fonts should map the lower-case special characters (á, é, í, ó, ú, ñ, ü) to their corresponding upper-case letter.
5. Save the changes.

Once you have translated the game and replaced the font files, you can run the game in Spanish and verify that the special characters are displayed correctly.

If you encounter any issues or have any questions, please refer to the game's documentation or contact the development team.

Happy translating and enjoy the game in Spanish!
