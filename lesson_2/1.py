a = int(input("введите первое число"))
b = int(input("введите второе число"))
if (a <b):
    return product(b,a)
elif (b !=0):
    return (a + product(a, b-1))
else:
    return 0
