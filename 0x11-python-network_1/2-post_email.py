#!/usr/bin/python3
import urllib.request as p
from urllib import parse
import sys
if __name__ == "__main__":
    data = {'email': sys.argv[2]}
    data = parse.urlencode(data).encode()
    x = p.Request(url=sys.argv[1], data=data)
    with p.urlopen(x) as r:
        print(r.read().decode('utf-8'))
