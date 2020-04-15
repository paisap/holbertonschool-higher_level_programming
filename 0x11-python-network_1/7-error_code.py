#!/usr/bin/python3
import requests
import sys
if __name__ == "__main__":
    x = requests.get(sys.argv[1])
    if x.status_code < 400:
        print(x.text)
    else:
        print("Error code: {}".format(x.status_code))
