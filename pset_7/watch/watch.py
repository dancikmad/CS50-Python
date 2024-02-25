"""
Program to extract URLs of YouTube videos that are embedded in HTML pages.

Example :
<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" 
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; 
encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Extracts : https://www.youtube.com/embed/xvFZjo5PgG0

Converts : https://youtu.be/xvFZjo5PgG0 (can be watched on YouTube itself)
"""

import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r"<iframe src=\"https?://(www\.)?youtube\.com/embed/([a-zA-Z0-9]+)\"></iframe>"
    if url_id := re.search(pattern, s):
        return f"https://youtu.be/{url_id.group(2)}"
    else:
        return None

if __name__ == "__main__":
    main()
