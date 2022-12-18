#! /usr/bin/env python

import requests
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-u", "--url", dest="url", help="Target URL to use for scanning (e.g. example.com)")
    parser.add_option("-w", "--wordlist", dest="wordlist", help="Wordlist used for subdomain mapping")
    (options, arguments) = parser.parse_args()
    if not options.url:
        parser.error("[-] Please specify a valid URL, use --help for more info")
    elif not options.wordlist:
        parser.error("[-] Please specify a valid wordlist, use --help for more info")
    else:
        return options


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass


options = get_arguments()
target_url = options.url
wordlist = options.wordlist

print()
print("-----------------------------------------------------")
print("Found subdomains from target: " + target_url)
print("-----------------------------------------------------")

with open(wordlist, "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = word + "." + target_url
        response = request(test_url)
        if response:
            print("[+] Discovered subdomain --> " + test_url)