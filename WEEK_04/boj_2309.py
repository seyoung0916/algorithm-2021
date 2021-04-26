height = []
for _ in range(9):
    height.append(int(input()))

heightSum = sum(height)  # 기존 난쟁이 키의 합

for i in range(8):  # 제거할 첫 번째 원소
    for j in range(i + 1, 9):  # 제거할 두 번째 원소
        if heightSum - (height[i] + height[j]) == 100:  # 두 원소를 제거한 키 합이 100일 경우
            first = height[i]  # 값을 저장
            second = height[j]
            break

# 제거할 원소를 변수 안에 저장하고 나와야 정상 작동 -> break가 하나의 for문만 빠져나와서
# 원소 제거
height.remove(first)
height.remove(second)
height.sort()

for i in height:
    print(i)
