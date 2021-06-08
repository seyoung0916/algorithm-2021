n, k = map(int, input().split())
coin = []  # 동전
res = {}
for _ in range(n):
    coin.append(int(input()))

for i in reversed(coin):  # 큰 동전부터 비교
    tmp = k // i
    res[i] = tmp  # 금액에 대한 동전 개수 append
    k = k % i

ans = 0
for key, value in res.items():
    ans += value
    
print(ans)
