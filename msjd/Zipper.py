# -*- coding:utf-8 -*-
'''基本字符串压缩
参与人数：153时间限制：3秒空间限制：32768K
通过比例：19.36%
最佳记录：0 ms|8552K （来自  xdzh）
题目描述

利用字符重复出现的次数，编写一个方法，实现基本的字符串压缩功能。比如，字符串“aabcccccaaa”经压缩会变成“a2b1c5a3”。若压缩后的字符串没有变短，则返回原先的字符串。
给定一个string iniString为待压缩的串(长度小于等于3000)，保证串内字符均由大小写英文字母组成，返回一个string，为所求的压缩后或未变化的串。
测试样例
"aabcccccaaa"
返回："a2b1c5a3"
"welcometonowcoderrrrr"
返回："welcometonowcoderrrrr"
'''

class Zipper:
    def zipString(self, iniString):
        # write code here
        if not iniString:
            return None
        lenth = len(iniString)
        if lenth == 0:
            return iniString
        res = []
        i = 0
        j = 1
        cnt = 1
        s = iniString[0]
        #a = iniString[0]
        while j < lenth:
            if iniString[i] == iniString[j]:
                cnt +=1
                j += 1 
            else:
                res.append(s)
                res.append(cnt)
                s = iniString[j]
                i = j
                j += 1
                cnt = 1
        res.append(s)
        res.append(cnt)
        if len(res) > lenth:
            return iniString
        else:
            return ''.join([str(i) for i in res])
        #print res
                

z = Zipper()
z.zipString('aabcccccaaa')


