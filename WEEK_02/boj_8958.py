n = int(input())

for _ in range(n):
    str = input()

    score = 0
    correct = 1  # O 누적 점수
    for i in str:

        if i == 'O':
            score += correct
            correct += 1
        else:
            correct = 1  # O점수 초기화

    print(score)
