n, k = map(int, input().split())
coins = []

for _ in range(n):
    coins.append(int(input()))

count_list = [0] * (k + 1)  # 0원으로 만들 수 있는 경우의 수로 시작
count_list[0] = 1  # 0원으로 0원 만드는 경우의 수 1

for i in coins:
    for j in range(i, k + 1):
        count_list[j] += count_list[j - i]  # 기존 j원을 만드는 경우 + (j-현재동전)의 금액을 만드는 경우의 수

print(count_list[k])
