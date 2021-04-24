def solution(citations):
    answer = 0
    citations.sort()
    # [6, 5, 3, 1, 0] -> 3
    # [31, 66] -> 2

    # [0, 0, 0] -> 0, [0, 1, 1] -> 1
    # [0, 1, 2] -> 1

    m = max(citations)

    for h in range(1, m + 1):  # h가 될 수 있는 수
        cnt = 0  # i번 이상 인용된 논문 개수
        flag = True
        for j in citations:
            if j >= h:  # h이상 인용된 논문 개수
                cnt += 1
            else:
                if j > h:  # j <= h이면 정상
                    flag = False
        if cnt >= h and flag:  # 참인 조건일 때 answer 갱신
            answer = h
        if not flag:  # 조건에 안맞으면 다음 수도 안 맞으므로 종료
            break
    return answer
