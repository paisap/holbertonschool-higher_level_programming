#!/usr/bin/python3
import requests
if __name__ == "__main__":
    x = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t - type: {}".format(type(x.text)))
    print("\t - content: {}".format(x.text))
