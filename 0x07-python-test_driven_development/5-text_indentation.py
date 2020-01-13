#!/usr/bin/python3
def text_indentation(text):
    m = 0
    if type(text) != str:
        raise TypeError("text must be a string")
    text1 = text.replace('?', '?\n\n')
    text1 = text1.replace('.', '?\n\n')
    text1 = text1.replace(':', '?\n\n')
    print("\n".join([i.strip() for i in text1.split("\n")]), end="")
