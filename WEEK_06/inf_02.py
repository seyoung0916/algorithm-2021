import json

durability = [5, 3, 4, 1, 3, 8, 3]
dog = [{
    "이름": "루비독",
    "나이": "95년생",
    "점프력": "3",
    "몸무게": "4",
}, {
    "이름": "피치독",
    "나이": "95년생",
    "점프력": "3",
    "몸무게": "3",
}, {
    "이름": "씨-독",
    "나이": "72년생",
    "점프력": "2",
    "몸무게": "1",
}, {
    "이름": "코볼독",
    "나이": "59년생",
    "점프력": "1",
    "몸무게": "1",
}]

'''
json_dog = json.dumps(dog, ensure_ascii=False) # 문자열로 변환
json_dog = json.loads(json_dog) # list로 변환됨
print(json_dog[0])
'''


def cross(arr, x):
    answer = [i['이름'] for i in dog]

    for i in dog:
        position = 0
        while position < len(durability) - 1:  # 돌의 위치를 벗어날 때까지
            position += int(i['점프력'])  # 점프력만큼 움직임
            durability[position - 1] -= int(i['몸무게'])  # 몸무게만큼 내구도가 줄어듬, 독이 0부터 시작하기 때문
            # 처음에 2칸을 뛰면 1인덱스의 돌에 도착하는 것
            if durability[position - 1] < 0:
                del answer[answer.index(i['이름'])]
                break
    return answer


print(cross(durability, dog))
