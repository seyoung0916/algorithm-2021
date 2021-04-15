t = int(input())

A = 300
B = 60
C = 10

a, b, c = 0, 0, 0

if t // A > 0:  # A 버튼 누를 수 있음
    a += t // A
    t %= A

if t // B > 0:
    b += t // B
    t %= B

if t // C > 0:
    c += t // C
    t %= C

if t == 0:
    print(a, b, c)
else:
    print(-1)
