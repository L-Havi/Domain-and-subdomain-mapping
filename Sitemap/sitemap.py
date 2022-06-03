#! /usr/bin/env python

import requests
import re
import urllib.parse

target_url = "Insert your target domain here"
target_links = []


def extract_links_from(url):
    response = requests.get(url)
    return re.findall(str('(?:href=")(.*?)"'), str(response.content))


def crawl(url):
    href_links = extract_links_from(url)
    for link in href_links:
        link = urllib.parse.urljoin(url, link)
        if '#' in link:
            link = link.split('#')[0]

        if url in link and link not in target_links:
            target_links.append(link)
            print(link)
            crawl(link)


crawl(target_url)
