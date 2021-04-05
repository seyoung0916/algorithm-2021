k, n, m = input().split()
k = int(k)
n = int(n)
m = int(m)

result = 0

if k * n > m:
    result = k * n - m
else:
    result = 0

print(result)