'''
给一个数列 S ,找出四个数 a,b,c,d 使得a + b + c + d = target。

分析：

跟之前的 2Sum, 3Sum 和 3Sum Closest 一样的做法，先排序，再左右夹逼，复杂度 O(n^3)。不过用 Python 可能会被卡超时。
先求出每两个数的和，放到 HashSet 里，再利用之前的 2Sum 去求。这种算法比较快，复杂度 O(n*n*log(n))，不过细节要处理的不少。
这里 C++ 用的是算法1， Java, Python 用的是 2。
这题 Java 可以好好地学学 HashMap 的使用， Python 可以学习 set, collection 和 itertools 的一些用法。

(2015-04-02 UPDATE)
这题解法 2 的复杂度是 O(n*n*log(n))，是在 HashMap 操作复杂度是 O(log(n)) 的情况下算出的。
不过是正常都把 HashMap 当成 O(1) 操作的，所以也会把总的复杂度算成 O(n*n)。

'''


import collections
import itertools
class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        two_sum = collections.defaultdict(list)
        ret = set()
        # itertools.combinations(enumerate(num), 2) 是求列表的排列组合，这里求的是组合。
        # print list(itertools.combinations([1,2,3,4],2))
        # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
        for (id1, val1), (id2, val2) in itertools.combinations(enumerate(num), 2):
            two_sum[val1 + val2].append({id1, id2})
        keys = two_sum.keys()
        for key in keys:
            if two_sum[key] and two_sum[target - key]:
                for pair1 in two_sum[key]:
                    for pair2 in two_sum[target - key]:
                        if pair1.isdisjoint(pair2):
                            ret.add(tuple(sorted([num[i] for i in pair1 | pair2])))
                del two_sum[key]
                if key != target - key:
                    del two_sum[target - key]
        return [list(i) for i in ret]