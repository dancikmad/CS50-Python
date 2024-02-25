"""
FIGlet, name after Frank, Ian and Glen's letters, is a program from the early 1990s 
for making large letters out of ordinary text, a form of ASCII art:

 _ _ _          _   _     _
| (_) | _____  | |_| |__ (_)___
| | | |/ / _ \ | __| '_ \| / __|
| | |   <  __/ | |_| | | | \__ \
|_|_|_|\_\___|  \__|_| |_|_|___/

Figlet has since been ported to Python as a module called pyfiglet.

Create a module figlet.py
-   Expects zero or two command-line arguments:
    -   Zero if the user would like to output text in a random font
    -   Two if the user would like to output text in a specific font, in which 
        case the first of the two should be
        -f or --font, and the second of the two should be the name of the font
-   Prompts the user for a str of text
-   Outputs that text in a desired font

*** If the user provides two command-line arguments and the first is not 
    -f or --font or the second is not the name of a font,
    the program should exit via sys.exit with an error message.
"""

import sys
from random import choice
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    available_fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        s = input("Input: ").strip()
        figlet.setFont(font=choice(available_fonts))
        print(figlet.renderText(s))

    elif len(sys.argv) == 3:
        if str(sys.argv[1]) in ["-f", "--font"] and str(sys.argv[2]) in available_fonts:
            s = input("Input: ").strip()
            figlet.setFont(font=str(sys.argv[2]))
            print(figlet.renderText(s))
        else:
            sys.exit("Invalid usage")

    else:
        sys.exit("Invalid usage")

if __name__ == "__main__":
    main()

