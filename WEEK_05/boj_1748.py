n = int(input())

num = [int('9' + '0' * i) for i in range(len(str(n)) - 1)]  # 120인 경우 1, 2자리일 때 개수 구함

start = 10 ** (len(str(n)) - 1)  # start 부터 n까지 자릿수만 알면 됨
answer = 0

for x, y in enumerate(num):  # x번째 원소 y
    answer += (x + 1) * y  # 길이가 x+1임

answer += (n - start + 1) * len(str(n))  # 마지막 범위

print(answer)
