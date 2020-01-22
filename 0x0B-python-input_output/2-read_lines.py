#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):
    with open(filename, encoding='UTF8') as file:
        f_lines = file.readlines()
        print(f_lines)
        if nb_lines >= len(f_lines) or nb_lines <= 0:
            for line in f_lines:
                print(line, end='')
        else:
            for i in range(nb_lines):
                print(f_lines[i], end='')
