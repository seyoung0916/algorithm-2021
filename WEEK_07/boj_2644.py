from collections import deque

n = int(input())  # 사람 수
a, b = map(int, input().split())  # a와 b의 촌수 구하기
m = int(input())  # 관계 수
rel = [[] for _ in range(n + 1)]  # 사람 1부터 시작
result = [0 for _ in range(n + 1)]  # 촌수계산용


def bfs(s):
    q = deque()
    visited = [False] * (n + 1)
    q.append(s)  # 시작

    while q:
        cur = q.popleft()

        for i in rel[cur]:
            if not visited[i]:
                visited[i] = True
                result[i] = result[cur] + 1
                q.append(i)


for _ in range(m):
    x, y = map(int, input().split())
    rel[x].append(y)
    rel[y].append(x)

bfs(a)

if result[b] != 0:
    print(result[b])
else:
    print(-1)
