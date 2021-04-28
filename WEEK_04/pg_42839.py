from itertools import permutations


def isPrime(num):
    if num == 0 or num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    answerNum = set()  # set 초기화
    arr = list(numbers)  # 문자열을 한 글자씩 split하려면 list로 형변환하면 됨

    for i in arr:  # 한 자리 숫자 체크
        if isPrime(int(i)):
            answerNum.add(int(i))

    for i in range(2, len(arr) + 1):
        p = list(permutations(arr, i))  # arr의 i개 순열을 구함

        for j in p:
            tmp = int(''.join(list(j)))
            if isPrime(tmp):
                answerNum.add(tmp)
    answer = len(answerNum)
    return answer
