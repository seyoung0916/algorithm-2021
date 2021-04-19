t = int(input())

for _ in range(t):
    n = int(input())

    max_amount = 0
    max_school = ''
    for _ in range(n):
        school, amount = input().split()
        amount = int(amount)

        if amount > max_amount:
            max_amount = amount
            max_school = school

    print(max_school)
    