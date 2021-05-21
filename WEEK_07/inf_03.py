'''입력
대기인원 = 14000605

출력
2025년 2월 413일 11시 0분 출발

입력
대기인원 = 1200202

출력
2020년 1월 1000일 11시 0분 출발'''

import datetime

today = datetime.datetime.today()
wait = 14000605


def solution(wait):
    days = 0  # 일년의 총 일수
    for i in range(10, 0, -1):
        days += 2 ** i  # 1~10월의 일수
    # wait // 1200은 총 대기일수
    year = (wait // 1200) // days  # 출발 년도
    remain_day = (wait // 1200) % days  # 남은 일수

    days_accumulate = 0
    month = 0
    for i in range(10, 0, -1):
        pre_days = days_accumulate  # 전달 일수
        days_accumulate += 2 ** i
        month += 1
        if days_accumulate > remain_day:
            break

    day = remain_day - pre_days
    wait_person = wait % 1200  # 마지막날 남은 인원(최종 남은 인원)
    hour = wait_person // 100 + 9  # 한 시간에 100명 태움, 9시부터 운행

    person_accumulate = [25, 40, 55, 70, 85, 100]  # 해당 분에 누적되는 탑승 인원
    remain_person = wait_person % 100 + 1  # 해당 시간에 남은 인원, 24명일 경우 둘은 다음 배에 타야해서 +1
    for i in person_accumulate:
        if i > remain_person:
            minute = person_accumulate.index(i) * 10
            break

    if wait_person % 100 == 99:  # 다음 시간 배를 타야 함
        hour += 1
        minute = 0

    if today.minute + minute > 60:
        minute = today.minute + minute - 60  # 시간은 현재를 사용
        hour += 1

    return f'{year + 2020}년 {month}월 {day}일 {hour}시 {minute}분 출발'


print(solution(wait))
