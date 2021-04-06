xcheck = {}
ycheck = {}

for i in range(3):
    a, b = input().split()
    a = int(a)
    b = int(b)

    if a in xcheck.keys():  # x좌표가 있으면
        xcheck[a] += 1
    else:
        xcheck[a] = 1  # 새로 추가

    if b in ycheck.keys():
        ycheck[b] += 1
    else:
        ycheck[b] = 1

x = y = 0
for key, value in xcheck.items():
    if value == 1:
        x = key
        break
for key, value in ycheck.items():
    if value == 1:
        y = key

print(x, y)
