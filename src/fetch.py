"""
This CLI program fetches URLs and caches them locally in the current directory.
You can view these links offline, since all assets are archived.

Additionally, it gathers metadata on the fetched content and can provide that
information if invoked with the --meta-data switch.

It can also fetch multiple links at a time.

Author: Noor Muhammad Malik
Date: Oct 25, 2021
License: None
"""
import requests

def fetch_url(url):
    """This function fetches the URL and caches it locally.
    :param url: a string with URL to fetch
    return: None"""
    # determine the filename by extracting the base URL
    filename = url.split('/')[2] + '.html'
    # initiate the request on the URL
    try:
        response = requests.get(url)
        with open(filename, 'w+') as f:
            f.write(str(response.content))
            print("[DEBUG] {} cached locally!".format(url))
    except Exception as e:
        print("Error in fetch_url!\n{}".format(e))
        exit(1)
    

def parse_metadata(url):
    """This function parses the locally cached URL data for metadata.
    :param url: a string which specifies the URL name to locate locally
        available file(s). 
    """
    pass