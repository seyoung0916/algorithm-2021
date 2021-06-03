import itertools


def solution(orders, course):
    answer = []

    for cnt in course:  # 세트메뉴 내 단품 제한
        combi = []  # 개수별 가능한 조합
        for menu in orders:
            tmp = list(itertools.combinations(menu, cnt))  # 가능한 조합
            for ul in tmp:
                if ul not in combi:
                    ul = sorted(list(ul)) # 최종적으로 오름차순으로 해야하므로
                    combi.append(ul)

        count = {}  # 조합에 대한 주문 건수 셈
        max_cnt = 0
        for g in combi:  # 가능한 조합(개수별)
            cnt = 0
            for order in orders:  # 한 메뉴
                flag = True  # 세트 된다고 가정
                for item in g:  # 단품메뉴
                    if order.find(item) == -1:  # 해당 단품이 없는 경우
                        flag = False
                        break
                if flag:  # 해당 메뉴에 item들이 모두 포함됨
                    cnt += 1
            if cnt >= 2:  # 최소 두명 이상에게 주문되어야 함
                count[''.join(g)] = cnt
                max_cnt = max_cnt if max_cnt > cnt else cnt  # max_cnt값 갱신

        for k, v in count.items():
            if v == max_cnt:
                answer.append(k)
    answer.sort()
    return answer


m = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
c = [2, 3, 5]
print(solution(m, c))
