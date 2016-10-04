# 232792560
def nod(x, y):
    if x > y:
        for j in range(1, y + 1):
            if x % j == 0 and y % j == 0:
                res = j
    else:
        for j in range(1, x + 1):
            if y % j == 0 and x % j == 0:
                res = j
    return res


def nok(x1, y1):
    return (x1 * y1) / (nod(x1, y1))

f = nok(11, nok(12, nok(13, nok(14, nok(15, nok(16, nok(17, nok(18, nok(19, 20)))))))))

print(f)