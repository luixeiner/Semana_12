def mayor (a, b, c):
    if ((a>b) and (a>c)):
        return a
    if ((b>a) and (b>c)):
        return b
    if ((c>a) and (c>b)):
        return c
print(mayor(18, 6, 14))