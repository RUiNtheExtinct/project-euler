from math import sqrt, floor

for i in range(2, 1000):
    d = False
    for j in range(1, i):
        c = i * i + j * j
        if sqrt(c) == floor(sqrt(c)) and sqrt(c) + i + j == 1000:
            print(i * j * sqrt(c))
            d = True
            break
        if d:
            break
    if d:
        break