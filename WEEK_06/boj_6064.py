n = int(input())


def solve(M, N, x, y):
    # x가 처음 만족하는 년도

    while x <= M * N:
        if x % N == y % N:
            return x
        x += M
    return -1


for _ in range(n):
    M, N, x, y = map(int, input().split())
    print(solve(M, N, x, y))
