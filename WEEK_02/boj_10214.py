T = int(input())

for _ in range(T):
    Y, G = 0, 0

    for _ in range(9):  # 9라운드
        y, g = input().split()

        y = int(y)
        g = int(g)

        Y += y
        G += g

    if Y > G:
        print('Yonsei')
    elif Y < G:
        print('Korea')
    else:
        print('Draw')
