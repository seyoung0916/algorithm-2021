N, K = map(int, input().split())
possible = list(map(int, input().split()))
angles = list(map(int, input().split()))

visit = [False] * 360  # 만들 수 있는 각도
q = []
q.append(possible[0])

while q:
    cur = q.pop(0)
    visit[cur] = True
    for p in possible:
        sub, add = cur - p, cur + p

        # 각도범위 체크
        if sub < 0:
            sub += 360
        if add >= 360:
            add -= 360

        if not visit[sub]:
            q.append(sub)
        if not visit[add]:
            q.append(add)

for angle in angles:
    if visit[angle]:
        print('YES')
    else:
        print('NO')
