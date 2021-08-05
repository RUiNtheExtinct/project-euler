t, ans = list(range(1, 101)), 0
for i in t:
    ans += i * i
print(ans - (sum(t) * sum(t)))
