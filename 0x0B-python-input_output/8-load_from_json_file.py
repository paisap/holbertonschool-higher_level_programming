#!/usr/bin/python3
import json


def load_from_json_file(filename):
    with open(filename, 'r') as f:
        try:
            x = json.load(f)
            return x
        except Exception as f:
            pass
