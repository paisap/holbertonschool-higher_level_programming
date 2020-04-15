#!/usr/bin/python3
import requests
import sys
if __name__ == "__main__":
    url = "https://api.github.com/user"
    x = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    try:
        print(x.json()['id'])
    except KeyError:
        print("None")
