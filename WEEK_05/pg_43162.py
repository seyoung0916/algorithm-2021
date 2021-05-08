def solution(n, computers):
    answer = 0
    visited = [False] * n

    def dfs(net, i):
        visited[i] = True

        for j in range(n):
            if net[i][j] and not visited[j]:  # 연결되어 있고 방문 안 한 노드일 경우
                dfs(net, j)

    for k in range(n):
        if not visited[k]:
            dfs(computers, k)
            answer += 1  # 한 네트워크 생성
    return answer
