str = input()

end = len(str) - 1  # str의 마지막 인덱스
flag = 1

for i in range(len(str) // 2):
    if str[i] != str[end]:
        flag = 0
        break
    end -= 1

print(flag)
