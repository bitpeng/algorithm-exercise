# coding:utf-8

import random
import time

t = time.time()

# 堆排序, 按照从小到大排序，所以建立大根堆
# 列表的第一个元素没有使用

def ShiftDown(a, i):
    if not a:
        return

    j = i
    #while j > 1:
    #    if a[j/2] < a[j]:
    #        a[j/2], a[j] = a[j], a[j/2]
    #    j /= 2
    N = len(a)
    while 2*j < N:  # 存在左孩子时
        ci = 2 * j # 左孩子节点下标
        if ci + 1 < N and a[ci] < a[ci + 1]: # ci保存左右孩子节点中大值的下标
            ci += 1

        if a[j] < a[ci]: # 和孩子互换，否则，该元素位置正确，可以退出
            a[j], a[ci] = a[ci], a[j]
        else:
            break
        j = ci


def BuildHeap(a):
    if not a:
        return

    i = len(a)/2
    while i >= 1:
        #print a[i]
        ShiftDown(a, i)
        i -= 1

def HeapSort(a):
    BuildHeap(a)
    b = []
    while len(a) > 1: # 列表的第一个元素没有使用
        a[1], a[-1] = a[-1], a[1]  # 将最大元素和最后一个元素互换，弹出最大元素，重新建造堆
        b.append(a.pop())
        BuildHeap(a)
    a = b[::-1]
    b.sort()
    print a == b
    #print b[::-1]
    #a[N - 1], a[0] = a[0], a[N - 1]


a = [random.randint(1,100) for i in range(1001)]
#a = [60, 39, 80, 25, 66, 3, 93, 92, 11, 11, 38]
print a
BuildHeap(a)
print a
HeapSort(a)
print time.time() - t
