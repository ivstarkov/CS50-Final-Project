
# Duplicate Remover

## Video Demo <https://youtu.be/OllvdoN2A9k>

## Description

Duplicate Remover removes or renames files with endings like " (1)", " - Copy", "- Copy (1)" etc.
If there are files with 'clear' name, for example "image001.jpg", all other files with similar names (e.g. "image001 (1).jpg") and same size will be removed. If there is no file with 'clear' name, one of duplicates will be renamed to 'clear' name and others will be deleted.
Program has GUI with 3 buttons and 3 fields. GUI is native to used system and window  is scallable. Upon start only one button active, 'Chose Directory'. User can chose desired directory either by pressing this button or by entering path into field and pressing 'Enter'. After chosing directory, second button, 'Analyze', become active. Pressing this button two lists of files appeared - files to be ranamed and files to be removed. After that user can continue by pressing 'Proceed' button and all supposed actions will be executed. Message with information about completition will appear after all the actions finished.

## Structure

Program written in Python 3.10. GUI created with Qt Designer and PyQt6 module. Programm converted to executable .exe file with auto-py-to-exe module. Program uses *os* and *re* libraries. Following RegEx exspression is used for duplicate selection: *r"(^\w+)(?: ?\(\d+\)| - Copy.*)(\.\w+)$"*\
All operations allocated into a separate file deleting.py and connected as a libruary to the main file.
Program uses five-file depth to look for duplicates.
