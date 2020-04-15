#!/usr/bin/python3
import requests
import sys
if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])
    x = requests.get(url)
    data = x.json()
    aux = 0
    try:
        for i in data:
            if aux == 10:
                break
            print("{}: {}".format(i['sha'], i['commit']['author']['name']))
            aux += 1
    except IndexError:
        pass
