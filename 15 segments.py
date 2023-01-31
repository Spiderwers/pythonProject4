def f(x, a1, a2):
    return ((a1 <= x <= a2) <= (430 <= x <= 490)) or (440 <= x <= 530)

m = 0
for a1 in range(400, 600):
    for a2 in range(a1 + 1, 600):
        if all(f(x, a1, a2) == 1 for x in range(400, 600)):
            m = max(m, a2 - a1)


print(m//10)
