#!/usr/bin/python3
import urllib.request as p
import sys
from urllib.error import URLError, HTTPError
if __name__ == "__main__":
    x = p.Request(sys.argv[1])
    try:
        with p.urlopen(x) as t:
            print(t.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
