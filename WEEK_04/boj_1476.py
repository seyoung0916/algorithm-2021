S, E, M = map(int, input().split())

s, e, m = 1, 1, 1
year = 1

while True:
    if S == s and E == e and M == m:
        break

    year += 1
    s += 1
    e += 1
    m += 1

    if s == 16:
        s = 1
    if e == 29:
        e = 1
    if m == 20:
        m = 1

print(year)
