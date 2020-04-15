#!/usr/bin/python3
import urllib.request as p
if __name__ == "__main__":
    with p.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print('\t- utf-8 content: {}'.format(html.decode('utf-8')))
