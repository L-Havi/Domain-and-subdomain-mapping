# Sitemapper & Subdomain Finder tools 

These tools allow you to discover target domains subdomains. Please these tools only with domains you have permission to scan

Subdomain finder uses a large wordlist file included in the same folder. Other wordlists can also be used

Sitemapper maps all links related to the domain and creates a map based on these links. (Unrelated links like link to youtube for example will be disregarded)

Python files work in any UNIX based operating systems and in Windows if Python is installed

Executables work even if Python is not installed

## Usage (EXE)

###### Subdomain Finder

```
Syntax: subdomain_mapper.exe [--help] [--url URL] [--wordlist WORDLIST]


[*] Options:
  -u URL, --url URL                                                          Specify the website's URL to use for sitemapping
  
  -w WORDLIST, --wordlist WORDLIST                                           Specify the wordlist used to discover subdomains

[*] Example:
  subdomain_mapper.exe -u example.com -w wordlist.txt                        This command starts discovering subdomains using base URL example.com 
                                                                             and wordlist wordlist.txt and displays subdomains it has found 

```

###### Sitemapper

```
Syntax: sitemap.exe [--help] [--url URL]

[*] Options:
  -u URL, --url URL                                   Specify the website's URL to use for sitemapping

[*] Example:
  sitemap.exe -u https://www.example.com              This command starts discovering the sitemap for the site www.example.com and displays it 

```

## Usage (Python Files)

###### Subdomain Finder

```
Syntax: python subdomain_mapper.py [--help] [--url URL] [--wordlist WORDLIST]


[*] Options:
  -u URL, --url URL                                                          Specify the website's URL to use for sitemapping
  
  -w WORDLIST, --wordlist WORDLIST                                           Specify the wordlist used to discover subdomains

[*] Example:
  python subdomain_mapper.py -u example.com -w wordlist.txt                  This command starts discovering subdomains using base URL example.com 
                                                                             and wordlist wordlist.txt and displays subdomains it has found 

```

###### Sitemapper

```
Syntax: python sitemap.py [--help] [--url URL]

[*] Options:
  -u URL, --url URL                                   Specify the website's URL to use for sitemapping

[*] Example:
  python sitemap.py -u https://www.example.com        This command starts discovering the sitemap for the site www.example.com and displays it 

```
