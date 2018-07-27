# coding:utf8
import re
from urllib.request import urlopen
import ssl

# SSLContext to avoid "SSL: CERTIFICATE_VERIFY_FAILED" Error
ssl._create_default_https_context = ssl._create_unverified_context

url = input("Url of website to scan : >> ") # https://lemonde.fr, https://tf1.fr

# Connect to a URL
website = urlopen(url)

# Read html code
html = website.read().decode("utf-8")

# Use re.findall to get all links
links = re.findall('"((http|ftp)s?://.*?)"', html)

print( "=====================" )
print( "links of", url, " : " )
print( "=====================" )
for link in links:
    print( link[0] )