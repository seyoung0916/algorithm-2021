n = input()

q1, q2, q3, q4, axis = 0, 0, 0, 0, 0

for _ in range(int(n)):
    a, b = input().split()

    a = int(a)
    b = int(b)

    if a == 0 or b == 0:
        axis += 1
    else:
        if a > 0 and b > 0:
            q1 += 1
        elif a < 0 and b > 0:
            q2 += 1
        elif a < 0 and b < 0:
            q3 += 1
        else:
            q4 += 1

print("Q1:", q1)
print("Q2:", q2)
print("Q3:", q3)
print("Q4:", q4)
print("AXIS:", axis)
