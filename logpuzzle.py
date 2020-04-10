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
if sys.version_info[0] >= 3:
    from urllib.request import urlretrieve
else:
    from urllib import urlretrieve

__author__ ='Sasha Lukas'

def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""
<<<<<<< HEAD

    url_list = []
    with open(filename) as file:
        for line in file:
            match = re.search('/puzzle/', line)
            if match:
                url = re.search(r'\S+puzzle+\S+.jpg', line)
                if url:
                    url_list.append(url.group(0))
    sorted_url_list = sorted(list(set(url_list)), key=lambda url: url)
    return sorted_url_list
    print(sorted_url_list)
=======
    # +++your code here+++
    with open(filename, 'r') as file:
        # file.close()

        url_list = []
        for line in file:
            match = re.search('puzzle', line)
            if match:
                url_result = re.search(r'\S+puzzle|S+.jpg', line)
                if url_result:
                    url_list.append(url_result.group())
        sorted_url = sorted(list(set(url_list)), key=lambda url: url[-8:-4])
        return sorted_url

>>>>>>> eb17f67c420cb6e6de91036ab97acaa6bd7e12ee



def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    # +++your code here+++
    if not os.path.exists(dest_dir):
<<<<<<< HEAD
        os.makedirs(dest_dir)
        print('dir made')
    index_html = '<html><body>'
    for index, url in enumerate(img_urls):
        image_name = 'img' + str(index)
        print('Retrieving {}'.format(url))
        urlretrieve(url, dest_dir + '/' + image_name)
        index_html += '<img src = {}></img>'.format(image_name)
    index_html += '</body></html>'
    with open(dest_dir + '/index.html', 'w') as write_index:
        write_index.write(index_html)
=======
        os.mkdir(dest_dir)

    f = open(os.path.join(dest_dir, 'index.html'), 'w')

    for i, url in enumerate(img_urls):
        print ('GET', url)
        img = 'img' + str(i)
        urllib.urlretrieve(url, os.path.join(dest_dir, img))
        f.write('<img src="' + img + '" />')

    f.close()
>>>>>>> eb17f67c420cb6e6de91036ab97acaa6bd7e12ee


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
