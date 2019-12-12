#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    t = sys.argv
    if len(sys.argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
    else:
        if t[2] == '+':
            print('{} + {} = {}'.format(t[1], t[3], add(int(t[1]), int(t[3]))))
        elif t[2] == '-':
            print('{} - {} = {}'.format(t[1], t[3], sub(int(t[1], int(t[3])))))
        elif t[2] == '*':
            print('{} * {} = {}'.format(t[1], t[3], mul(int(t[1], int(t[3])))))
        elif t[2] == '/':
            print('{} / {} = {}'.format(t[1], t[3], div(int(t[1], int(t[3])))))
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            sys.exit(1)
