def f1(n):
    if n <= 0:
        return 1
    else:
        return 1 + f1(n-5)

print(f1(11))