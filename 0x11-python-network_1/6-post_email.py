#!/usr/bin/python3
import requests
import sys
if __name__ == "__main__":
    x = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(x.text)
