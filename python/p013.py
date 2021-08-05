p, c = [], 0
for i in range(100):
    p.append(input()[::-1])
ans = ""
for i in range(50):
    a = 0
    for j in range(100):
        a += int(p[j][i])
    a += c
    a, c = a % 10, a // 10
    ans += str(a)
ans = ans[::-1]
ans = str(c) + ans
print(ans[:10])