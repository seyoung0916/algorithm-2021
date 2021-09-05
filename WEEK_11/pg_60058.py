from collections import deque


def isbalanced(p):
    if p[0] == ')':  # 닫힌 괄호로 시작하면 올바르지 않은 경우
        return False
    else:
        return True


def splitP(p):
    q = deque()
    idx = 0

    q.append(p[idx])
    idx += 1

    # 균형잡힌 괄호까지의 인덱스를 구하고 split
    while q:
        cur = q.popleft()
        nx = p[idx]

        if cur == nx:  # 다음 괄호가 현재 괄호와 같으면 균형잡힌 괄호 상태가 아님
            q.append(cur)
            q.append(nx)
        idx += 1

    u = p[:idx]
    v = p[idx:]
    return u, v


def solve(p):
    if p == "":  # 1: 빈 문자열인 경우
        return ""

    u, v = splitP(p)  # 2: 균형잡힌 문자열 u, v로 분리

    if isbalanced(u):  # u가 올바른 문자열인 경우
        return u + solve(v)  # 3-1: v에 대한 수행
    else:  # 4
        str = "("  # 4-1
        str += solve(v)  # 4-2
        str += ")"  # 4-3
        u = u[1:-1]  # 4-4
        for x in u:
            if x == '(':
                str += ')'
            else:
                str += '('
        return str  # 4-5


def solution(p):
    answer = solve(p)

    return answer
