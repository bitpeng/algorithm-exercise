#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

'''
  题目描述:
  我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重
  叠地覆盖一个2*n的大矩形，总共有多少种方法？
'''

'''
  观察题目中的矩形，2*n的，是个长条形。本来脑中想象的是复杂的华容道，但是既然只是简单的长条形，那么依然逆向分析。既然是长条形的，那么从后向前，最后一个矩形2*2的，只有两种情况：

　　第一种是最后是由一个2*(n-1)的矩形加上一个竖着的2*1的矩形
　　另一种是由一个2*(n-2)的矩形，加上两个横着的2*1的矩形
　　因此我们可以得出，
　　第2*n个矩形的覆盖方法等于第2*(n-1)加上第2*(n-2)的方法。使用代码可以表示为：
    for(i=3;i<71;i++){
        arr[i] = arr[i-1]+arr[i-2];
    }
'''

# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        n = number
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        a = 1
        b = 2
        for i in range(3, n + 1):
            a, b = b, a + b
        return b


s = Solution()
for i in range(1,10):
    print s.rectCover(i)
