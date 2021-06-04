from bisect import bisect_left
from itertools import combinations


def make_cases(tmp):
    cases = []  # 지원자에 대한 쿼리 도출
    for k in range(5):  # 0~4개의 -가 올 수 있음
        for li in combinations([0, 1, 2, 3], k):  # 1인자는 -가 올 수 있는 인덱스, 무작위로 k개를 뽑음
            q = ''  # 생성될 쿼리
            for i in range(4):
                if i in li:
                    q += '-'
                else:
                    q += tmp[i]
            cases.append(q)
    return cases


def solution(info, query):
    answer = []
    all = {}
    for i in info:  # 지원자 정보
        tmp = i.split()
        cases = make_cases(tmp)
        for case in cases:  # 점수를 제외한 가능 쿼리
            if case in all.keys():  # 키값 존재
                all[case].append(int(tmp[-1]))
            else:
                all[case] = [int(tmp[-1])]  # 겹치는 앞 쿼리가 있을 수 있으므로 점수만 append

    for key in all.keys():  # 오름차순으로 정리해 bisect_left로 시간 단축축
        all[key].sort()

    for q in query:
        tmp = q.split()
        target = tmp[0] + tmp[2] + tmp[4] + tmp[6]  # 점수를 제외한 조건
        score = int(tmp[7])

        if target in all.keys():
            answer.append(len(all[target]) - bisect_left(all[target], score, lo=0, hi=len(all[target])))
        else:
            answer.append(0)

    return answer
