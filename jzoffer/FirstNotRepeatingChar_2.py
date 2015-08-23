# -*- coding:utf-8 -*-

# 答案错误:您提交的程序没有通过所有的测试用例

# 测试用例:
# "google"

# 对应输出应该为:
# "ggg#ll"

class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        from collections import OrderedDict
        if not s:
            return -1
 
        # 以字符作为键, 以出现次数作为值
        d = OrderedDict()
        ret = []
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
                for k in d:
                    if d[k] == 1:
                        ret.append(i)
                        break
                else:
                    ret.append('#')
                        
        return ret
                #ret.append(i)
                
 
        ## print d
        ## 把第一次出现一次的字符记录下来
        #k = None
        #for i in d:
        #    if d[i] == 1:
        #        # print i
        #        k = i
        #        break
        ## print 'k: ', k
        #if k is None:
        #    return -1
        #for i in range(len(s)):
        #    print s[i], k
        #    if s[i] == k:
        #        return i
        #return '#'