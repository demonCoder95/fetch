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
import time
from bs4 import BeautifulSoup

class URLMetadata():
    def __init__(self, site="", num_links=0, images=0, last_fetch=""):
        self.site = site
        self.num_links = num_links
        self.images = images
        self.last_fetch = last_fetch

class URLFetcher():
    def __init__(self, url=""):
        self.url = url
        # an object to store the last_fetch time
        self.url_metadata = URLMetadata()

    def fetch_url(self):
        """This function fetches the URL and caches it locally.
        :param url: a string with URL to fetch
        return: None"""
        # determine the filename by extracting the base URL
        self.base_url = self.url.split('/')[2]
        filename = self.base_url + '.html'
        # initiate the request on the URL
        try:
            response = requests.get(self.url)
            # record the fetch time in the metadata struct
            self.url_metadata.last_fetch = time.asctime()
            with open(filename, 'w') as f:
                f.write(str(response.content))
        except Exception as e:
            print("Error in fetch_url!\n{}".format(e))
            exit(1)
        
    def parse_metadata(self):
        """This function parses the locally cached URL data for metadata.
        :param url: a string which specifies the URL name. 
        """
        # store the site entry
        self.url_metadata.site = self.base_url
        # fetch last fetch time is updated by the fetching function
        # count links and store in metadata object
        self.url_metadata.num_links = self._count_links()
        # count images and store in the metadata object
        self.url_metadata.images = self._count_images()

    def print_metadata(self):
        """This function prints the metadata stored in the URLMetadata
        object."""
        print(f'site: {self.url_metadata.site}')
        print(f'num_links: {self.url_metadata.num_links}')
        print(f'images: {self.url_metadata.images}')
        print(f'last_fetch: {self.url_metadata.last_fetch}')

    def _count_links(self):
        """Helper function to count links in an HTML source file."""
        a_tags = list()
        # open the HTML file for parsing
        with open(self.base_url + '.html', 'r') as f:
            soup = BeautifulSoup(f, 'html.parser')
            a_tags = soup.find_all('a')        
        return len(a_tags)

    def _count_images(self):
        """Helper function to count images in an HTML source file."""
        img_tags = list()
        with open(self.base_url + ".html", 'r') as f:
            soup = BeautifulSoup(f, 'html.parser')
            img_tags = soup.find_all('img')
        return len(img_tags)

