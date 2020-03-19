#!/usr/bin/python3
import sys


load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file


f = "add_item.json"
try:
    y = load_from_json_file(f)
except Exception:
    y = []
for i in range(1, len(sys.argv)):
    y.append(sys.argv[i])
save_to_json_file(y, f)
