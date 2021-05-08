def solution(numbers, target):
    answer = 0

    def dfs(idx, res):
        if idx == len(numbers):  # 끝까지 돔
            if res == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx + 1, res + numbers[idx])
            dfs(idx + 1, res - numbers[idx])

    dfs(0, 0)
    return answer
