This python script allows you to discover target domains subdomains. Please this script only with domains you have permission to scan

It uses a large wordlist file included in the same folder. Other wordlists can also be used

It works in any UNIX based operating systems and in Windows if Python is installed

## Usage

```
Syntax: python subdomain_mapper.py [--help] [--url URL] [--wordlist WORDLIST]


[*] Options:
  -u URL, --url URL                                                          Specify the website's URL to use for sitemapping
  
  -w WORDLIST, --wordlist WORDLIST                                           Specify the wordlist used to discover subdomains

[*] Example:
  python subdomain_mapper.py -u example.com -w wordlist.txt                  This command starts discovering subdomains using base URL example.com 
                                                                             and wordlist wordlist.txt and displays subdomains it has found 

```
