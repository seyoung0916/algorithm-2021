N = int(input())

for i in range(N):
    r, e, c = input().split()
    r = int(r)
    e = int(e)
    c = int(c)

    if r > e - c:
        print("do not advertise")
    elif r == e - c:
        print("does not matter")
    else:
        print("advertise")
