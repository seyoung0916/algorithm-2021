from collections import deque

m, n, h = map(int, input().split())
box = [[[i for i in map(int, input().split())] for _ in range(n)] for _ in range(h)]
visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]


def bfs():
    while q:
        l, r, c = q.popleft()
        # 여섯 방향 체크
        for i in range(6):
            nl = l + dh[i]
            nx = r + dx[i]
            ny = c + dy[i]

            # 범위 체크 및 토마토가 있는 위치
            if h > nl >= 0 and n > nx >= 0 and m > ny >= 0 and box[nl][nx][ny] == 0:
                box[nl][nx][ny] = box[l][r][c] + 1  # 기존 토마토 값 + 1
                q.append((nl, nx, ny))


# 익은 토마토를 큐에 저장
q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                q.append((i, j, k))

bfs()

flag = True
for i in box:  # 층
    for j in i:  # 줄
        if 0 in j:
            flag = False  # 안 익은 토마토 존재

if flag:
    res = 0
    for i in box:
        for j in i:
            tmp = max(j)
            res = max(res, tmp)
    print(res - 1)  # 처음 토마토가 1로 세팅되어있어 1을 빼야 일수가 나옴
else:
    print(-1)
