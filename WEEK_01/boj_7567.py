str = input()

height = 0

for i in range(len(str)):
    if i > 0:
        if str[i] != str[i - 1]:  # 이전 그릇과 방향 다름
            height += 10
        else:
            height += 5
    else:  # 첫 그릇
        height += 10

print(height)
