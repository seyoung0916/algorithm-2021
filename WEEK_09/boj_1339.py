import operator

n = int(input())
dic = {}
alpha = []
for _ in range(n):
    x = input()
    alpha.append(x)
    l = len(x) - 1  # 자리수
    for i, k in enumerate(list(x)):
        d = 10 ** (l - i)

        if k in dic:  # 알파벳을 가진 key가 있는 경우
            dic[k] += d
        else:
            dic[k] = d
    # value로 내림차순 정렬
    dic = dict(sorted(dic.items(), key=operator.itemgetter(1), reverse=True))

# 알파벳 -> 숫자 매칭
num = 9
for i, k in dic.items():
    dic[i] = num
    num -= 1
answer = 0
for a in alpha:
    a_list = list(a)
    b = [str(dic[x]) for x in a_list]
    answer += int(''.join(b))

print(answer)