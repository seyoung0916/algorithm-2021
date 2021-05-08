n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

tetromino = [
    [(0, 0), (0, 1), (1, 0), (1, 1)],  # ㅁ
    [(0, 0), (0, 1), (0, 2), (0, 3)],  # ㅡ
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (1, 0), (2, 0), (2, 1)],  # ㄴ
    [(0, 1), (1, 1), (2, 1), (2, 0)],
    [(0, 0), (1, 0), (2, 0), (0, 1)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 0)],
    [(0, 0), (0, 1), (0, 2), (1, 2)],
    [(1, 0), (1, 1), (1, 2), (0, 2)],
    [(1, 0), (1, 1), (1, 2), (0, 0)],
    [(0, 0), (0, 1), (0, 2), (1, 1)],  # ㅜ
    [(0, 1), (1, 0), (1, 1), (1, 2)],
    [(1, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (1, 0), (2, 0), (1, 1)],
    [(0, 0), (0, 1), (1, 1), (1, 2)],  # ㄴ+|
    [(0, 1), (0, 2), (1, 0), (1, 1)],
    [(0, 1), (1, 1), (1, 0), (2, 0)],
    [(0, 0), (1, 0), (1, 1), (2, 1)]
]


def count(x, y):
    global answer
    for i in range(len(tetromino)):
        result = 0
        for j in range(4):
            try:
                nx = x + tetromino[i][j][0]
                ny = y + tetromino[i][j][1]
                result += board[nx][ny]
            except IndexError:
                break
        answer = max(answer, result)


answer = 0

for i in range(n):
    for j in range(m):
        # 기준점 i, j
        count(i, j)

print(answer)
