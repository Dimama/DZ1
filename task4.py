# -*- coding: utf-8 -*-
# 906609
# count - количество разрядов множителей

def max_palindrome_number(count):
    res = 0
    for i in range(10**(count-1), 10**count):
        for j in range(10**(count-1), 10**count):
            if is_palindrome(i*j) and i*j > res:
                res = i*j
    return res


# num - исследуемое число, count - число разрядов числа
def is_palindrome(num):
    buf = num
    reverse = 0
    while buf > 0:
        reverse = reverse*10 + buf % 10
        buf //= 10

    return num == reverse


print(max_palindrome_number(3))
