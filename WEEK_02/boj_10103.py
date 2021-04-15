r = int(input())

a, b = 100, 100
for _ in range(r):
    x, y = input().split()
    x = int(x)
    y = int(y)

    if x == y:
        continue
    elif x > y:
        b -= x
    else:
        a -= y

print(a)
print(b)
