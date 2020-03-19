#!/usr/bin/python3
import sys


load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file


x = []
y = []
f = "add_item.json"
for i in range(1, len(sys.argv)):
    x.append(sys.argv[i])
try:
    y = (load_from_json_file(f))
except Exception as t:
    pass
for i in y:
    x.append(i)
save_to_json_file(x, f)
