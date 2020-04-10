#!/usr/bin/env python2
"""
Logpuzzle exercise

Copyright 2010 Google Inc.
Licensed under the Apache License, Version 2.0
http://www.apache.org/licenses/LICENSE-2.0

Google's Python Class
http://code.google.com/edu/languages/google-python-class/

Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"

"""

import os
import re
import sys
import urllib
import argparse


__author__ ='Sasha Lukas + instructors +stackoverflow'

def url_sort_key(s):
    return s.split('-')[-1]

def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""

    # url_list = []
    # with open(filename, 'r') as file:
    #     for line in file:
    #         match = re.search('/puzzle/', line)
    #         if match:
    #             url = re.search(r'\S+puzzle+\S+.jpg', line)
    #             if url:
    #                 url_list.append(url.group(0))
    # sorted_url_list = sorted(list(set(url_list)), key=lambda url: url)
    # return sorted_url_list
    # print(sorted_url_list)

    domain = re.search(r'_(.+)', filename).group(1)
    matches = set()

    with open(filename, 'r') as file:
        for line in file:
            match = re.search(r'GET (\S+) HTTP', line)
            if match:
                if "puzzle" in match.group(1):
                    matches.add("http://" + domain + match.group(1))

    return sorted(set(matches), key=url_sort_key)


def download_images(img_urls, dest_dir):
    """
    
    """
    # +++your code here+++
    # See if dest_dir exists--if not, create it
    if not os.path.isdir(dest_dir):
        os.makedirs(dest_dir)

    # Build HTML
    html_parts = ["<html><body>"]

    for i, url in enumerate(img_urls):
        try:
            # Download image
            ufile = urllib.urlopen(url)
            img = ufile.read()
            f = open("./%s/img%d" % (dest_dir, i), 'wb')
            # f = open('{}index.html'.format(dest_dir, i), 'wb')
            f.write(img)
            f.close()

            # Add image tag
            html_parts.append('<img src="img%d">' % i)
        except IOError:
            print('problem reading url:', url)

    html_parts.append("</body></html>")

    # Write HTML file
    f = open('./' + dest_dir + '/index.html','w')
    f.write(''.join(html_parts))
    f.close()


def create_parser():
    """Create an argument parser object"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--todir',  help='destination directory for downloaded images')
    parser.add_argument('logfile', help='apache logfile to extract urls from')

    return parser


def main(args):
    """Parse args, scan for urls, get images from urls"""
    parser = create_parser()

    if not args:
        parser.print_usage()
        sys.exit(1)

    parsed_args = parser.parse_args(args)

    img_urls = read_urls(parsed_args.logfile)

    if parsed_args.todir:
        download_images(img_urls, parsed_args.todir)
    else:
        print('\n'.join(img_urls))


if __name__ == '__main__':
    main(sys.argv[1:])
