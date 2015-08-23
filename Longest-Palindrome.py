# coding:utf-8
import random

''' 由于是要求最长的回文串，所以我们可以从最长的子串开始遍历。当找到一个回文串后，就可以直接返回
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

print check("1", 0, 1)
s = ''.join([str(random.randint(0, 20)) for i in range(10)])
#s = ''.join([str(i) for i in range(10)])
print s
print LongestPalindrome(s)
