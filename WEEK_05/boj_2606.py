n = int(input())  # 컴퓨터 수
b = int(input())  # 연결된 쌍의 수

visited = [False] * (n + 1)  # 0번은 안 씀
net = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
answer = 0

# 연결 정보를 net에 저장
for _ in range(b):
    a, b = map(int, input().split())
    net[a][b] = 1
    net[b][a] = 1


def dfs(arr, idx):
    visited[idx] = True  # 방문처리
    global answer
    answer += 1

    tmp = arr[idx]  # idx의 연결정보
    for x in range(1, len(tmp)):
        if tmp[x] and not visited[x]:  # 연결 and 방문 안한 컴퓨터
            dfs(arr, x)


dfs(net, 1)
print(answer - 1)  # 1번 컴퓨터는 제외
