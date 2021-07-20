from itertools import combinations

a, b = map(int, input().split())
st = input().split()
answer = []

st.sort()
tmp = list(combinations(st, a))

for item in tmp:
    v = 0  # 모음 개수
    for x in item:
        if x in ['a', 'e', 'i', 'o', 'u']:
            v += 1
    c = a - v  # 자음 개수
    if v >= 1 and c >= 2:
        answer.append(''.join(list(item)))

for i in answer:
    print(i)
