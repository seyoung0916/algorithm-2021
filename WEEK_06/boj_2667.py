from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n = int(input())
map = [[x for x in map(int, list(input()))] for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
answer = []
danji = 0


def bfs(x, y):
    cnt = 0  # 해당 단지 내 아파트 개수
    queue = deque()
    queue.append((x, y))  # 시작점

    while queue:
        cnt += 1

        cur_x, cur_y = queue.popleft()
        visited[cur_x][cur_y] = True
        for z in range(4):
            nx = cur_x + dx[z]  # 다음 체크할 인덱스
            ny = cur_y + dy[z]

            if nx < 0 or nx >= n:
                continue
            if ny < 0 or ny >= n:
                continue
            if not visited[nx][ny] and map[nx][ny]:
                queue.append((nx, ny))

        queue = deque(set(list(queue)))

    global answer
    answer.append(cnt)


for i in range(n):
    for j in range(n):
        if map[i][j] == 0:
            visited[i][j] = True
        else:
            if not visited[i][j]:
                danji += 1
                bfs(i, j)

print(danji)
for i in sorted(answer):
    print(i)
