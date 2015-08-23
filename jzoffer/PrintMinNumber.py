# -*- coding:utf-8 -*-
import random

str = unicode
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        lenth = max([len(str(i)) for i in numbers])
        for i in range(len(numbers)):
            item = numbers[i]
            l = len(str(item))
            if l != lenth:
                numbers[i] = str(item)
                numbers[i] += (lenth - l) * u'a'
            else:numbers[i] = str(item)
        numbers.sort()
        print numbers
        s = u''
        for i in numbers:
            s += i
        return s.replace(u'a', '')

      
s = Solution()
#numbers = [random.randint(1, 100) for i in range(4)]
#numbers = [1, 3, 23, 43, 6]
numbers = [3,32,321]
print s.PrintMinNumber(numbers)


# -*- coding:utf-8 -*-
import random

str = unicode
class Solution:
    def PrintMinNumber(self, numbers):
        n = [str(i) for i in numbers]
        while True:
            i[0] for i in n
    

