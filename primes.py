def MakePrime(n):
    if n <= 1:
        return []

    ret = [2, 3]
    i = 5
    while i <= n:
        for j in [item for item in ret if item * item <= i]:
            if i % j == 0: #or j * j > i:
                break
                #flag = False
        else:
            ret.append(i)
        i += 2

    return ret

print MakePrime(1000)
