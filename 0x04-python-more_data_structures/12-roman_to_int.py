#!/usr/bin/python3
def roman_to_int(roman_string):
    matrix = [
            ['I', 'V', 'X', 'L', 'C', 'D', 'M'],
            [1, 5, 10, 50, 100, 500, 100]]
    j = 0
    l = 7
    result = 0
    if roman_string == None:
        return 0
    if str(roman_string) == False:
        return 0
    for i in roman_string:
        j = 0
        for m in matrix[0]:
            if i == m:
                if l < j:
                    result = matrix[1][j] - result
                else:
                    result += matrix[1][j]
                l = j
                j = 0
            else:
                j += 1
    return result
