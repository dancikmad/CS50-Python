"""
python3 -m pip install emoji

import emoji module

Prompt the user for a (Str)
Store (Str) in a variable

output the "emojized" version of that (Str), converting any codes or aliasses 
therein to their corresponding emoji.

"""

import emoji

prompt = input("Input: ")
print("Output: {}".format(emoji.emojize(prompt, language="alias")))
