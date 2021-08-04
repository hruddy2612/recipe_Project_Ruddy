# recipe_Project_Ruddy

_**Overview**_
====================

1. ``main.py`` contains functions and the code, this runs the app

1. ``images folder`` this contains all of the images needed and the 
cvs file which contains the database for the recipes 

1. ``doc folder`` contains the base code I created before creating the function for the GUI

_**Requirements**_
====================

Python 3.7 or higher
Pillows version v2021.7.7 was used
tkinter newest version

_**Installation**_
====================

use ``pip`` to install the required third party packages: pip -r requirements.txt

ensure ``pillows`` and ``tkinter`` are installed

_**Usage**_
====================

``main.py`` run it in the project root folder

``images folder`` images and csv file must be in the same file for GUI to run properly, if 
the location of this file changes, the file source must also be changed in the code

_**Known issues**_
====================

Limitations include:

1. number of recipes in the csv, searching for recipes is limited due to the way the code matches the input with the database
1. placement of widgets in tkinter is limited due to grid not being compatible with pack, so pack and place were used over 
grid placement. 

