N = int(input())
result = 0  # 가장 작은 값으로 초기화

for i in range(N):
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)

    if a == b and b == c:  # 모두 같을 경우
        if result < (10000 + 1000 * a):
            result = 10000 + 1000 * a  # 상금
    elif a == b or a == c:  # 두 개가 같을 경우
        if result < (1000 + a * 100):
            result = 1000 + a * 100
    elif b == c:
        if result < (1000 + b * 100):
            result = 1000 + b * 100
    else:  # 셋 다 다른 값
        maxNum = max(a, b, c)
        if result < maxNum * 100:
            result = maxNum * 100

print(result)
