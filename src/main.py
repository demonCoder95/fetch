"""Main driver CLI program for the module written in fetch.py."""

import argparse
import fetch

# program description
description = """This program fetches URLs and caches the assets locally for
later browsing and viewing. It can also gather additional metadata with invoked
with the --metadata flag."""

# initiate a parser
parser = argparse.ArgumentParser(description=description)

# add the URL arguments
parser.add_argument('urls', metavar='URLs', type=str, nargs='+',
    help='URLs to fetch')

# add the --metadata flag
parser.add_argument('--metadata', action='store_true',
    help='get metadata for the URLs as well'
)

# parse the arguments on the CLI
args = parser.parse_args()

# Fetch all URLs passed to the program
for each_url in args.urls:
    fetch.fetch_url(each_url)
