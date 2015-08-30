# coding:utf-8
from random import randint
import time

t = time.time()

def ShellSort(a):
    if not a:
        return
    N = len(a);
    gap = N / 2;
    while gap > 0:
        i = gap
        while i < N:
            j = i - gap
            while j >= 0 and a[j] > a[j + gap]:
                a[j], a[j + gap] = a[j + gap], a[j]
                j -= gap
            i += 1
            # i++就是这一行的调试，话费了我的好多时间啊！
        gap /= 2
        #print gap

a = [randint(1,1000) for i in range(100000)]
# print a
ShellSort(a)
b = a[:]
a.sort()
print a == b
print time.time() - t
