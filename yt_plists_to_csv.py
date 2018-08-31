#!/usr/bin/python
# Copyright 2018 stringCode ltd.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

import sys
import os
import re
import csv

"""YouTube playlist name & url extractor

Extracts names and urls form YouTube playlist html page. Writes them to csv.
"""

def main():
    # Handle args
    args = sys.argv[1:]
    if not args:
        print 'usage: file'
        sys.exit(1)
    
    # Load file to variable
    f = open(args[0], 'rU')
    html = f.read()
    f.close()

    # Extract name and url from html
    pattern = r'<h3.*\n.*<a.+href="(.+)".*>(.+)</a>.*\n.*</h3'
    a_tags_matches = re.findall(pattern, html)
    playlists = []
    for match in a_tags_matches:
        (url, name) = match
        playlists.append((url, name))

    # Write to csv
    output_file_name = os.path.splitext(args[0])[0] + ".csv"
    f = open(output_file_name, "w")
    w = csv.writer(f)
    w.writerow(["name", "url"])
    for (url, name) in playlists:
        w.writerow([name, url])
    f.close()

if __name__ == '__main__':
  main()


