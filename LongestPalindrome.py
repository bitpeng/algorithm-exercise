# coding:utf-8

import random
import time

####################################################################

'''
     由于是要求最长的回文串，所以我们可以从最长的子串开始遍历。当找到一个回文串后，就可以直接返回
     了。不用再遍历那些短的子串了。
     对于字符串s, 假设串长度为N,判断过程如下：
    1. 最长的子串就是本身，所以判断s是不是子串。假如不是，进行下一步：
    2. 然后判断串长度为N - 1的子串是不是，即：s[:N - 1], s[1:]
    3. 依次进行下一轮判断.直到找到个是回文串的子串。
'''
# 判断s的子串:"s[i], s[i+1]... s[j]"是否是回文的
def check(s, i, j):
    tmp = s[i:j + 1]
    #print tmp
    #return tmp == tmp.reverse()
    return tmp == tmp[::-1]

def LongestPalindrome(s):
    if not s:
        return "", 0
    lenth = len(s)
    diffLen = lenth - 1
    #maxPalindrome = ""
    while diffLen >= 0:
        i = 0
        j = diffLen
        while j < lenth:
             if check(s, i, j):
                return  s[i:j+1], diffLen + 1
             i += 1
             j += 1
        diffLen -= 1

####################################################################

'''求最长回文子串的Manacher方法'''
def LongestPalindrome_v2(s):
    if not s:
        return ""
    tmp = '#' + '#'.join(s) + '#'
    p = [0 for i in tmp]
    p[0] = 1; p[1] = 2;
    maxLen = 1        # 保存最大长度
    idi = 1; mx = 2   # 初始化，最长回文串中心下标为1(第二个字符), 右边界下标为2
    for i in range(2, len(tmp)):
        j = 2 * idi - i
        if mx > i:
            if mx - i > p[j]:
                p[i] = p[j]
            else:
                p[i] = mx - 1
        else:
            p[i] = 1
        while tmp[i + p[i]] == tmp[i - p[i]]:
            p[i] += 1

        if p[i] - 1 > maxLen:
            maxLen = p[i] - 1
            idi = i
            mx = idi + maxLen - 1

####################################################################

def LongestPrefix(s1, s2):
    if not s1 or not s2:
        return 0, ""
    i = 0
    n1 = len(s1); n2 = len(s2)
    while i < n1 and i < n2 and s1[i] == s2[i]:
        i += 1
    return i, s1[:i]

def LongestRepeatSubstring(s):
    if not s:
        return ""
    a = [s[i:] for i in range(len(s))]
    a.sort()
    ret = 0; retstr = ""
    for i in range(len(a) - 1):
        tmp, substr = LongestPrefix(a[i], a[i + 1])
        if tmp > ret:
            ret = tmp; retstr = substr
    return ret, retstr

''' 直接拼接求最长重复子串的方法不对，还是那个问题，
    两个比较的后缀可能都来自一个串，这就不对了'''
def LongestPalindrome_v3(s):
    if not s:
        return 0, ""
    ss = s + s[::-1]
    return LongestRepeatSubstring(ss)

s="abbacdefcdefcd"
print LongestPalindrome_v3(s)
print LongestPalindrome(s);print

def test():
    #while True:
    for i in range(10):
        s = [chr(random.randint(97, 100)) for i in range(10)]
        s = ''.join(s)
        print s
        print LongestPalindrome_v3(s)
        print
        time.sleep(2)

####################################################################

def LongestPrefix_2(s1, s2):
    if not s1 or not s2:
        return 0, ""
    if '#' in s1 and '#' in s2: # 他们的后缀不能来自于同一个串
        return 0,""
    if '#' not in s1 and '#' not in s2:
        return 0, ""
    i = 0
    n1 = len(s1); n2 = len(s2)
    while i < n1 and i < n2 and s1[i] == s2[i]:
        i += 1
    return i, s1[:i]

def LongestRepeatSubstring(s):
    if not s:
        return ""
    a = [s[i:] for i in range(len(s))]
    a.sort()
    ret = 0; retstr = ""
    for i in range(len(a) - 1):
        tmp, substr = LongestPrefix_2(a[i], a[i + 1])
        if tmp > ret:
            ret = tmp; retstr = substr
    return ret, retstr

class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        # write your code here
        if not A or not B:
            return 0
        s = A + "#" + B
        ret, retstr = LongestRepeatSubstring(s)
        return ret, retstr
'''
    转化问题：求s和s[::-1]的最长公共子串，利用后缀数组求.
    注意，后缀数组比较时不能来自同一个串
'''
def LongestPalindrome_v4(s):
    so = Solution()
    print so.longestCommonSubstring(s, s[::-1])
LongestPalindrome_v4(s)

####################################################################
