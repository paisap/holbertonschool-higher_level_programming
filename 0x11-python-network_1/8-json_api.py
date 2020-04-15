#!/usr/bin/python3
import requests
import sys
if __name__ == "__main__":
    q = "" if len(sys.argv) < 2 else sys.argv[1]
    x = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})
    try:
        if x.json():
            print("[{}] {}".format(x.json()["name"], x.json()["id"]))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
