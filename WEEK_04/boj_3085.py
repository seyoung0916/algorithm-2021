N = int(input())
candy = [[x for x in map(str, input())] for _ in range(N)]

dx, dy = [0, 1], [1, 0]

answer = 0


def checkAnswer(arr):
    global answer
    for i in range(N):  # 가로로 연속된 사탕 개수를 구함
        tmp = 1
        for j in range(1, N):
            if arr[i][j - 1] == arr[i][j]:
                tmp += 1
            else:
                answer = tmp if tmp > answer else answer
                tmp = 1
        answer = tmp if tmp > answer else answer  # 한 줄이 모두 같은 경우 answer 갱신이 안 돼서 따로 처리

    for i in range(N):  # 세로로 연속된 사탕 개수를 구함
        tmp = 1
        for j in range(1, N):
            if arr[j - 1][i] == arr[j][i]:
                tmp += 1
            else:
                answer = tmp if tmp > answer else answer
                tmp = 1
        answer = tmp if tmp > answer else answer  # 한 줄이 모두 같은 경우


for i in range(N):
    for j in range(N):
        for z in range(2):  #
            nx, ny = i + dx[z], j + dy[z]
            # 범위 넘어갈 경우 패스
            if nx >= N or ny >= N:
                continue
            candy[i][j], candy[nx][ny] = candy[nx][ny], candy[i][j]
            checkAnswer(candy)
            candy[i][j], candy[nx][ny] = candy[nx][ny], candy[i][j]  # 원위치

print(answer)
