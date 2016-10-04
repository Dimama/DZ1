# 6857
def largest_prime_factor(n):
    c = 2
    while c ** 2 <= n:
        if n % c == 0:
            n /= c
            res = c
        else:
            c += 1

    if n > res:
        res = int(n)

    return res

print(largest_prime_factor(600851475143))
