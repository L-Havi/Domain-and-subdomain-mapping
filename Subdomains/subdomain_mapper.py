 /usr/bin/env python

import requests


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass


target_url = "insert a domain you are mapping here"

with open("subdomains-wordlist.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = target_url + "/" + word
        response = request(test_url)
        if response:
            print("[+] Discovered subdomain --> " + test_url)
