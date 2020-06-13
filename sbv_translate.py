# sbv_translate.py

# NOTE: used pyinstaller to create a single executable file
# pyinstaller -F sbv_translate.py
# there is a problem with pyinstaller
# (I had to include this file for the executable to run)
import pkg_resources.py2_warn

# Import the argparse library to handle command line arguments
import argparse

# Import to check on file names and open/write files
import os
import sys

# Import to create an easy way to skip to every 3rd value in an array
import numpy as np

# Import google translate package
import googletrans
from googletrans import Translator

# list of lanuages on 6/10/2020
# LANGUAGES = {
#     'af': 'afrikaans',
#     'sq': 'albanian',
#     'am': 'amharic',
#     'ar': 'arabic',
#     'hy': 'armenian',
#     'az': 'azerbaijani',
#     'eu': 'basque',
#     'be': 'belarusian',
#     'bn': 'bengali',
#     'bs': 'bosnian',
#     'bg': 'bulgarian',
#     'ca': 'catalan',
#     'ceb': 'cebuano',
#     'ny': 'chichewa',
#     'zh-cn': 'chinese (simplified)',
#     'zh-tw': 'chinese (traditional)',
#     'co': 'corsican',
#     'hr': 'croatian',
#     'cs': 'czech',
#     'da': 'danish',
#     'nl': 'dutch',
#     'en': 'english',
#     'eo': 'esperanto',
#     'et': 'estonian',
#     'tl': 'filipino',
#     'fi': 'finnish',
#     'fr': 'french',
#     'fy': 'frisian',
#     'gl': 'galician',
#     'ka': 'georgian',
#     'de': 'german',
#     'el': 'greek',
#     'gu': 'gujarati',
#     'ht': 'haitian creole',
#     'ha': 'hausa',
#     'haw': 'hawaiian',
#     'iw': 'hebrew',
#     'hi': 'hindi',
#     'hmn': 'hmong',
#     'hu': 'hungarian',
#     'is': 'icelandic',
#     'ig': 'igbo',
#     'id': 'indonesian',
#     'ga': 'irish',
#     'it': 'italian',
#     'ja': 'japanese',
#     'jw': 'javanese',
#     'kn': 'kannada',
#     'kk': 'kazakh',
#     'km': 'khmer',
#     'ko': 'korean',
#     'ku': 'kurdish (kurmanji)',
#     'ky': 'kyrgyz',
#     'lo': 'lao',
#     'la': 'latin',
#     'lv': 'latvian',
#     'lt': 'lithuanian',
#     'lb': 'luxembourgish',
#     'mk': 'macedonian',
#     'mg': 'malagasy',
#     'ms': 'malay',
#     'ml': 'malayalam',
#     'mt': 'maltese',
#     'mi': 'maori',
#     'mr': 'marathi',
#     'mn': 'mongolian',
#     'my': 'myanmar (burmese)',
#     'ne': 'nepali',
#     'no': 'norwegian',
#     'ps': 'pashto',
#     'fa': 'persian',
#     'pl': 'polish',
#     'pt': 'portuguese',
#     'pa': 'punjabi',
#     'ro': 'romanian',
#     'ru': 'russian',
#     'sm': 'samoan',
#     'gd': 'scots gaelic',
#     'sr': 'serbian',
#     'st': 'sesotho',
#     'sn': 'shona',
#     'sd': 'sindhi',
#     'si': 'sinhala',
#     'sk': 'slovak',
#     'sl': 'slovenian',
#     'so': 'somali',
#     'es': 'spanish',
#     'su': 'sundanese',
#     'sw': 'swahili',
#     'sv': 'swedish',
#     'tg': 'tajik',
#     'ta': 'tamil',
#     'te': 'telugu',
#     'th': 'thai',
#     'tr': 'turkish',
#     'uk': 'ukrainian',
#     'ur': 'urdu',
#     'uz': 'uzbek',
#     'vi': 'vietnamese',
#     'cy': 'welsh',
#     'xh': 'xhosa',
#     'yi': 'yiddish',
#     'yo': 'yoruba',
#     'zu': 'zulu',
#     'fil': 'Filipino',
#     'he': 'Hebrew'
# }

# Create the parser
my_parser = argparse.ArgumentParser(prog='sbv_translate',
                                    description='Translate an SubViewer .sbv subtitle file from English to another \
                                                language using Google Translate',
                                    epilog='Enjoy the program! :)')
# Add the arguments
my_parser.add_argument('--input',
                       action='store',
                       required=True,
                       help='Input file: An English language SubViewer(.sbv) caption file')

my_parser.add_argument('--output',
                       action='store',
                       required=True,
                       help='Output file: A Google Translated SubViewer(.sbv) caption file')

my_parser.add_argument('--language',
                       action='store',
                       required=True,
                       help='Language string from GoogleTranslate. Choose from the short names in the list below: \t' + str(googletrans.LANGUAGES))

# Execute the parse_args() method
args = my_parser.parse_args()

# check if the language is in the list
if not args.language in googletrans.LANGUAGES.keys():
    print('The language specified is not supported by Google Translate. Choose a language code from the following list:')
    print(googletrans.LANGUAGES)
    sys.exit()

if not os.path.isfile(args.input):
    print('The input file specified does not exist')
    sys.exit()

# warn that you are going to overwrite the files
if os.path.isfile(args.output):
    print('Warning: The output file specified exists. It will be overwritten.')
    # @TODO Add a Y/N question here
    # sys.exit()

# NOTE: We are taking an ".sbv" file and translating the captions
#       The file format is below. 3 lines for each caption.
#       1) timestamp
#       2) caption
#       3) blank line
#
# [Example SubViewer(.sbv) caption file]
# 0:00:00.599,0:00:04.160
# >> ALICE: Hi, my name is Alice Miller and this is John Brown
#
# 0:00:04.160,0:00:06.770
# >> JOHN: and we're the owners of Miller Bakery.
#
# 0:00:06.770,0:00:10.880
# >> ALICE: Today we'll be teaching you how to make
# our famous chocolate chip cookies!
#
# 0:00:10.880,0:00:16.700
# [intro music]
#
# 0:00:16.700,0:00:21.480
# Okay, so we have all the ingredients laid out here
#
# <<EOF>>

# read in the file to translate line by line into an array
with open(args.input, 'r') as f2:
  lineList = f2.readlines()

# build caption text to send to Google Translate
# Getting length of list = lines in the text file
length = len(lineList)

# create a list of numbers to iterate over
# in the input file: (1) timecode; (2) caption text; (3) blank line
# numpy.arange(start, stop, step)
n = np.arange(0,length,3)
# iterate over time stamps - Start at 0 and do every third line
times = ""
for x in np.nditer(n):
    times += lineList[x]

# numpy.arange(start, stop, step)
n = np.arange(1,length,3)
#iterate over captions - Start at 1 and do every third line
captions = ""
for x in np.nditer(n):
    captions += lineList[x]

file_translate = Translator()
result = file_translate.translate(captions, dest=args.language)

# create lists to iterate through from the text
timeLines = times.splitlines()
transLines = result.text.splitlines()

# initialize the loop
x = 0
lenLines = len(timeLines)

with open(args.output, 'w') as f:
    while x < lenLines:
        f.write(timeLines[x])
        f.write("\n")
        f.write(transLines[x])
        f.write("\n\n")
        x += 1
