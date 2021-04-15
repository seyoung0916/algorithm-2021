while True:
    n = int(input())

    if n == -1:
        break

    arr = []  # 약수를 넣음
    sum = 0  # 약수 합

    for i in range(1, n):  # 1~n-1까지
        if n % i == 0:  # i가 약수
            arr.append(i)
            sum += i

    if sum == n:  # 완전수
        tmp = ' + '.join(map(str, arr))
        tmp = str(n) + ' = ' + tmp
        print(tmp)
    else:
        print(str(n) + ' is NOT perfect.')
