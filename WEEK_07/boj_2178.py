from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
n, m = map(int, input().split())
maze = [[x for x in map(int, list(input()))] for _ in range(n)]

end_x = n - 1
end_y = m - 1

q = deque()
q.append((0, 0))

while q:
    cur_x, cur_y = q.popleft()

    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:  # 이동 가능
            maze[nx][ny] = maze[cur_x][cur_y] + 1
            q.append((nx, ny))

print(maze[end_x][end_y])