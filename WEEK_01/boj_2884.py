h, m = input().split()
h = int(h)
m = int(m)

flag = False  # 시간 설정에 대한 플래그

m -= 45  # 45분을 뺌
if m < 0:
    m += 60
    flag = True

if flag:  # 시간을 빼야하는 경우
    h -= 1
    if h < 0:
        h += 24

print(h, m)