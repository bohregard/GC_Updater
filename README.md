GC_Updater
==========

Simple python updater for adobe flash and java using back ends such as webparser, beautifulsoup, selenium, and _winreg.

The userinput.py is where the code is run from and fetches the contents based on the Downloads.txt file. After the program is completed the file is written.

The program's main agenda is to download the files and if necessary (provided from user input) install the programs silently in the background.

Currently the program assumes that a dropbox location exists at C:\Dropbox. This will be changed in a future update to read the dropbox location from the .db file.

The following programs are fetched for:

Java
Adobe Flash
SuperAntiSpyware Tech Addition


Added support for Ccleaner, silverlight and Adobe Reader will come in the future as the project progresses.