N = int(input())
vote = []

str = input()
for i in range(N):
    vote.append(str[i])

a = vote.count('A')
b = vote.count('B')

if a > b:
    print('A')
elif a < b:
    print('B')
else:
    print('Tie')
