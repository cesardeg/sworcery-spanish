## Modification of Font Files to Support Special Characters in the Game

This README.md file describes the changes made to the game's font files in order to properly support special characters. In particular, a modification was made to the "Conduit ITC" font to ensure that texts are always displayed in uppercase.

### Problem Description

In the game, when using the "Conduit ITC" font, the text is transformed into uppercase. However, it cannot convert special characters, which remain in lowercase. This limitation results in inconsistency within the uppercase text, particularly in languages that rely on these special characters. For instance, the word "Cáucaso" would be converted as "CáUCASO" instead of "CÁUCASO" due to the lowercase representation of the letter "Á". While the game successfully capitalizes most of the text, it faces difficulties with special characters.

![Problematic special characters](../proof/before.PNG)

### Implemented Solution

To solve this issue, the following approach was taken:

1. Special characters present in the game that required proper rendering were identified.

2. The lowercase special characters were replaced with their corresponding uppercase versions in the font files (conduit_itc.fnt, conduit_itc_2x.fnt, conduit_itc_4x.fnt).

3. Relevant attributes of the characters in the XML font files were modified. The attributes that were updated include: "x", "y", "width", "height", "xoffset", "yoffset", "xadvance", "page", and "chnl".

![Fixed special characters](../proof/after.PNG)

### Example of Modification

Let's take the character "á" (Unicode 225) as an example and observe how its attributes were substituted with their corresponding uppercase variant "Á" (Unicode 193) in the conduit_itc.fnt font.

Before modification:
```xml
<char id="193" x="53" y="0" width="8" height="14" xoffset="0" yoffset="0" xadvance="7" page="0" chnl="15" />
...
<char id="225" x="20" y="45" width="6" height="11" xoffset="0" yoffset="3" xadvance="7" page="0" chnl="15" />
```

After modification:
```xml
<char id="193" x="53" y="0" width="8" height="14" xoffset="0" yoffset="0" xadvance="7" page="0" chnl="15" />
...
<char id="225" x="53" y="0" width="8" height="14" xoffset="0" yoffset="0" xadvance="7" page="0" chnl="15" />
```

### Correspondence Table of Modified Characters

The following table displays the characters that were replaced and their corresponding Unicode decimal codes:


| Character | Code | Replaced | Code |
|-----------|------|----------|------|
| À         | 192  | à        | 224  |
| Á         | 193  | á        | 225  |
| Â         | 194  | â        | 226  |
| Ã         | 195  | ã        | 227  |
| Ä         | 196  | ä        | 228  |
| Å         | 197  | å        | 229  |
| Æ         | 198  | æ        | 230  |
| Ç         | 199  | ç        | 231  |
| È         | 200  | è        | 232  |
| É         | 201  | é        | 233  |
| Ê         | 202  | ê        | 234  |
| Ë         | 203  | ë        | 235  |
| Ì         | 204  | ì        | 236  |
| Í         | 205  | í        | 237  |
| Î         | 206  | î        | 238  |
| Ï         | 207  | ï        | 239  |
| Ð         | 208  | ð        | 240  |
| Ñ         | 209  | ñ        | 241  |
| Ò         | 210  | ò        | 242  |
| Ó         | 211  | ó        | 243  |
| Ô         | 212  | ô        | 244  |
| Õ         | 213  | õ        | 245  |
| Ö         | 214  | ö        | 246  |
| Ø         | 216  | ø        | 248  |
| Ù         | 217  | ù        | 249  |
| Ú         | 218  | ú        | 250  |
| Û         | 219  | û        | 251  |
| Ü         | 220  | ü        | 252  |
| Ý         | 221  | ý        | 253  |
| Þ         | 222  | þ        | 254  |
| ß         | 223  | ß        | 223  |
| Ÿ         | 376  | ÿ        | 255  |
| Œ         | 338  | œ        | 339  |
| Š         | 352  | š        | 353  |

Test string ÀàÁáÂâÃãÄäÅåÆæ Çç ÈèÉéÊêËë ÌìÍíÎîÏï ÐðÑñ ÒòÓóÔôÕõÖöØø ÙùÚúÛûÜü ÝýÞþßŸÿŒœŠš

![Test Conduit font with special characters](../proof/test-conduit.PNG)
![Test Arial font with special characters](../proof/test-arial.PNG)

### Conclusions

With the modifications made to the font files, special characters are now rendered correctly in uppercase, aligning with the style of the rest of the game's text. This provides a more consistent and cohesive gaming experience for players.

Fortunately, all this special characters are also supported in the other font used in the game, Arial Narrow, which is featured in "The Megatome."

As a result of these modifications, the game now fully supports translations in French, Spanish, Italian, Portuguese, German, Swedish, Norwegian, Danish, Finnish and Icelandic. Players can enjoy a seamless experience with correctly displayed text in these languages.
