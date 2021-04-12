while True:
    a, b = input().split()
    a = int(a)
    b = int(b)

    if a == 0 and b == 0:
        break

    if b % a == 0:  # a가 b의 약수
        print('factor')
    elif a % b == 0:  # a가 b의 배수
        print('multiple')
    else:
        print('neither')
