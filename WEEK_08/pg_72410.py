import re


def solution(new_id):
    answer = ''

    answer = new_id
    answer = answer.lower()
    answer = re.sub('[^a-z0-9\-_.]', '', answer)
    answer = re.sub('\.+', '.', answer)  # .이 한 번 이상 반복될 경우 치환
    answer = re.sub('^[.]|[.]$', '', answer)  # 양끝 . 제거
    answer = 'a' if len(answer) == 0 else answer[:15]
    answer = re.sub('[.]$', '', answer)  # 끝 . 제거
    answer = answer if len(answer) > 2 else answer + ''.join([answer[-1] for i in range(3 - len(answer))])

    return answer


'''
    new_id = new_id.lower()
    for x in new_id:
        # 조건에 맞는 문자의 경우
        if 'a' <= x <= 'z' or '0' <= x <= '9' or (x == '-' or x == '_' or x == '.'):
            answer += x

    new_id = answer
    answer = ''
    for x in new_id:
        # 이번에 추가해야 할 문자가 .인 경우
        if answer and x == '.':
            # 현재 맨 마지막 원소가 .인 경우
            if answer[len(answer) - 1] == '.':
                continue
        answer += x

    if answer:
        if answer[0] == '.':
            answer = answer[1:]
    if answer:
        if answer[len(answer) - 1] == '.':
            answer = answer[:-1]

    if not answer:  # 빈 문자열
        answer = 'a'

    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    if len(answer) <= 2:
        while len(answer) != 3:
            answer += answer[len(answer) - 1]
'''

print(solution("abcdefghijklmn.p"))
