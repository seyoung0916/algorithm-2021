from collections import deque


def bfs():
    while q:
        cur = q.popleft()
        if cur == "123456789":
            print(dic[cur])
            return
        k = cur.find('9')  # 9의 인덱스
        x, y = k // 3, k % 3  # 이중배열에서의 9 위치

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= 3 or ny < 0 or ny >= 3:
                continue
            nidx = nx * 3 + ny  # 합친 문자에서 바뀔 9의 인덱스
            list_cur = list(cur)
            list_cur[k], list_cur[nidx] = list_cur[nidx], list_cur[k]  # 바뀌는 자리와 치환
            str_next = ''.join(list_cur)  # 바뀐 상태의 문자열
            if not dic.get(str_next):  # 이전에 바뀐 상태가 없으면
                dic[str_next] = dic[cur] + 1  # 회전 횟수 증가
                q.append(str_next)
    print(-1)


puzzle = [list(map(int, input().split())) for _ in range(3)]
dic = dict()  # 숫자:회전횟수 담음
q = deque()

for i in range(3):
    for j in range(3):
        if not puzzle[i][j]:  # 0을 9로 치환
            puzzle[i][j] = 9

tmp = ''
for p in puzzle:
    tmp += ''.join(map(str, p))
dic[tmp] = 0
q.append(tmp)
bfs()
