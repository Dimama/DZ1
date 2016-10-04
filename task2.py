#4613732
def sum_fibon(limit):
    res = 0
    num1 = 1
    num2 = 1
    num3 = 0
    while num3 < limit:
        num3 = num2 + num1
        num1 = num2
        num2 = num3
        if not (num3 % 2):
            res += num3
    return res

print(sum_fibon(4e6))