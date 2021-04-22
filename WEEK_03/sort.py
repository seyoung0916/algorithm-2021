import random

# 버블정렬
a = random.sample(range(1, 10), 5)
print("=== bubble ===")
print(a)  # 정렬 전
n = len(a)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print(a)

# 삽입정렬
a = random.sample(range(1, 10), 5)
print("=== insertion ===")
print(a)
n = len(a)
for i in range(1, n):
    key = a[i]  # 기준 값
    j = i - 1  # 바로 이전 위치
    while j >= 0 and a[j] > key:  # 몇 번째 자리에 값을 넣어야 하는지 찾음
        a[j + 1] = a[j]
        j -= 1  # 맨 앞까지 체크
    a[j + 1] = key
print(a)

# 선택정렬
a = random.sample(range(1, 10), 5)
print("=== selection ===")
print(a)
n = len(a)
for i in range(n):
    min_idx = i
    for j in range(i + 1, n):
        if a[min_idx] > a[j]:  # 최솟값 인덱스를 찾음
            min_idx = j
    a[i], a[min_idx] = a[min_idx], a[i]
print(a)

# 퀵정렬
a = random.sample(range(1, 100), 10)
print("=== quick ===")
print(a)


def quickSort(a, start, end):
    if start < end:
        left = start
        pivot = a[end]

        for i in range(start, end):
            if a[i] < pivot:  # 리스트의 인덱스 값이 pivot보다 작을 경우
                a[i], a[left] = a[left], a[i]
                left += 1
        a[left], a[end] = a[end], a[left]
        quickSort(a, start, left - 1)
        quickSort(a, left + 1, end)


quickSort(a, 0, len(a) - 1)
print(a)
