# sbv_translate
Simple program to use Google Translate to convert English SubViewer (.sbv) files to other languages.
=======

## Features
  * Command line way to translate an english sbv file
  * Google Translate
    * access to all of the google languages
    * same api that website uses
    * `NOTE:` there is a character limit

### Installation
The following packages were used. If you are using a virtual environment you can install them with pip. `googletrans` and `numpy` are the keys. This code also pulls in `argparse`, but it did not show up as a pip package needed in the virtual environment I was using.
```
Package     Version
----------- ----------
altgraph    0.17
certifi     2020.4.5.2
chardet     3.0.4
googletrans 2.4.0
idna        2.9
macholib    1.14
numpy       1.18.5
PyInstaller 3.6
requests    2.23.0
urllib3     1.25.9
```

#### Requirements File
“Requirements file” contains a list of items to be installed using pip.

You can install all dependencies for the  by running `pip install -r requirements.txt` from the root of the project.
```
pip install -r requirements.txt
```

#### Executable
“dist” contains an MacOS executable version of the script. It was created by using PyInstaller.

You can create this on Mac or Windows by running `pyinstaller -F sbv_translate.py` from the root of the project.
```
pyinstaller -F sbv_translate.py
```
