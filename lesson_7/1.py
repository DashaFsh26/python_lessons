def sum(a, b):
    return a + b

sum(sum(1, 3), sum(4, 4))

sum(sum(1, 3), 8)
sum(4, 8)
12


result = sum(sum(1, 3), sum(sum(4, 2), 3))

print(result)  # 