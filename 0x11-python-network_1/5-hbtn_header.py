#!/usr/bin/python3
import requests
import sys
if __name__ == "__main__":
    x = requests.get(sys.argv[1])
    print(x.headers.get('X-Request-Id'))
