from math import gcd

t = list(range(1, 21))
print(t)
ans = 1
for i in t:
    if ans % i:
        ans = (ans * i) // gcd(ans, i)
print(ans)
