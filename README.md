<<<<<<< HEAD
# sbv-translate
Use Google Translate to convert English SubViewer (.sbv) files to other languages
=======
# sbv_translate

Simple program to use Google Translate to convert English SubViewer (.sbv) files to other languages.

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
certifi     2020.4.5.2
chardet     3.0.4
googletrans 2.4.0
idna        2.9
numpy       1.18.5
pip         20.1.1
requests    2.23.0
setuptools  47.1.1
urllib3     1.25.9
wheel       0.34.2
```

#### Requirements File
“Requirements file” containsa list of items to be installed using pip.

You can install all dependencies for the  by running `pip install -r requirements.txt` from the root of the project.
```
pip install -r requirements.txt
```
>>>>>>> Initial commit
