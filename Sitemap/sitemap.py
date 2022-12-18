#! /usr/bin/env python

import optparse
import requests
import re
import urllib.parse

target_links = []


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-u", "--url", dest="url", help="Target URL to use for scanning (e.g. https://www.example.com)")
    (options, arguments) = parser.parse_args()
    if not options.url:
        parser.error("[-] Please specify a valid URL, use --help for more info")
    else:
        return options


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


options = get_arguments()

target_url = options.url

print()
print("-----------------------------------------------------")
print("Found URLs from target: " + target_url)
print("-----------------------------------------------------")
crawl(target_url)
