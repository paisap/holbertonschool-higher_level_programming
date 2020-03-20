#!/usr/bin/python3
def pascal_triangle(n):
    lis_t = []
    aux = []
    cont = 2
    h = 0
    p = 0
    if n <= 0:
        return lis_t
    lis_t.append([1])
    for i in range(n - 1):
        for j in range(cont):
            if j == 0:
                aux.append(1)
            elif j + 1 == cont:
                aux.append(1)
            else:
                aux.append(lis_t[h][p] + lis_t[h][p + 1])
                p += 1
        h += 1
        p = 0
        cont += 1
        lis_t.append(aux)
        aux = []
    return lis_t
