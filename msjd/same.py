# coding:utf-8

'''
    确定两串乱序同构
    参与人数：114时间限制：3秒空间限制：32768K
    通过比例：41.89%
    最佳记录：0 ms|8552K （来自  渭水涟漪）
    题目描述

    给定两个字符串，请编写程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。这里规定大小写为不同字符，且考虑字符串重点空格。
    给定一个string stringA和一个string stringB，请返回一个bool，代表两串是否重新排列后可相同。保证两串的长度都小于等于5000。
    测试样例：
    "This is nowcoder","is This nowcoder"
    返回：true
    "Here you are","Are you here"
    返回：false
'''

class Same:
    def checkSam(self, stringA, stringB):
        # write code here
        al = stringA.split()
        bl = stringB.split()
        al.sort()
        bl.sort()
        return al == bl



s = Same()
print s.checkSam('here you are', 'Here you are')
