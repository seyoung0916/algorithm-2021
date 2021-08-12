from collections import deque


def bfs():
    while q:
        x, cnt = q.popleft()
        print(x, cnt)
        for dx in [-1, 1, x] : # 왼, 오, 순간이동
            nx = x + dx
            if nx <0 or nx >100000 :
                continue



n, k = map(int, input().split())
visit = False*100000
dic = dict()  # 이동 횟수와 방법법

bfs(n, 0, visit)
