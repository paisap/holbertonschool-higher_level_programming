#!/usr/bin/python3
import urllib.request as p
import sys
if __name__ == "__main__":
    with p.urlopen(sys.argv[1]) as response:
        print(response.getheader('X-Request-Id'))
