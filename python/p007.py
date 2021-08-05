p, c, n, s = [2, 3, 5, 7, 11, 13], 6, 10001, 17
while c < n:
    b = True
    for i in p:
        if s % i == 0:
            b = False
            break
    if b:
        p.append(s)
        c += 1
    s += 2
print(p[-1], len(p))