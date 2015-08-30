# coding:utf-8

import random
import time

t = time.time()

# 快速排序的分割算法, 参考自编程珠玑
# [l, r]为闭区间
def partion(a, l, r):
    # tmp = a[0]
    if l >= r:
        return
    m = l
    #for i in range(1, len(a)):
    for i in range(l + 1, r + 1):
        if a[i] < a[l]:
            m += 1
            a[m], a[i] = a[i], a[m]

    a[l], a[m] = a[m], a[l]
    partion(a, l, m - 1)
    partion(a, m + 1, r)
    return m

#def qsort():
if __name__ == "__main__":
    N = 100000
    a = [random.randint(1,100000) for i in range(N)]
    partion(a, 0, N - 1)
    print a
    b = a[:]; a.sort()
    print b == a
    print time.time() - t

