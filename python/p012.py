def div(n):
    d = {}
    i = 1
    while i * i <= n:
        if n % i == 0:
            d[i] = 1
            d[n // i] = 1
        i += 1
    return len(d)


ans, n = 0, 1
d = int(input())
while ans < d:
    ans = div((n * (n + 1)) // 2)
    n += 1
n -= 1
print((n * (n + 1)) // 2)
