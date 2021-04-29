def solution(brown, yellow):
    answer = []
    x = 3
    while True:
        y = brown // 2 - x + 2

        if x >= y and (x - 2) * (y - 2) == yellow:
            answer.append(x)
            answer.append(y)
            break
        x += 1

    return answer