N = int(input())
vote = []

for i in range(N):
    vote.append(int(input()))

a = vote.count(0)
b = vote.count(1)

# N이 홀수라 같을 경우는 없음
if a > b:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')
