# 233168
def multi_sum(count):
    summa = 0
    for number in range(count):
        if not  (number % 3) or not (number %5):
            summa += number
    return summa

print(multi_sum(1000))