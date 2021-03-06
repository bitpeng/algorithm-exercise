import random
import time

'''
def LongestPrefix_2(s1, s2):
    if not s1 or not s2:
        return 0, ""
    if '#' in s1 and '#' in s2:
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
'''

t = time.time()
def LongestPrefix(s1, s2):
    if not s1 or not s2:
        return 0, ""
    i = 0
    n1 = len(s1); n2 = len(s2)
    while i < n1 and i < n2 and s1[i] == s2[i]:
        i += 1
    return i, s1[:i]

'''
    这里开始的思路是想求A，B的后缀数组的最长公共子串, 但是发现不对，
    因为比较的连个子串来自一个串，所以不对
'''
class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        # write your code here
        if not A or not B:
            return 0
        # s = A + "#" + B
        s = [A[i:] for i in range(len(A))] + [B[i:] for i in range(len(B))]
        #print s
        s.sort()
        #print s
        ret = 0; retstr = ""
        for i in range(len(s) - 1):
            tmp, substr = LongestPrefix(s[i], s[i + 1])
            if tmp > ret:
                ret = tmp; retstr = substr
        return ret, retstr

so = Solution()
print so.longestCommonSubstring("abcdefcdefcd", "cdef")




#print LongestRepeatSubstring("abcdefcdef")
#print LongestRepeatSubstring("abcdefcdefc")
#print LongestRepeatSubstring("abcdefcdefcd")
#s = ''.join([chr(random.randint(97, 105)) for i in range(5000)])
##print s
#print LongestRepeatSubstring(s)
#print time.time() - t
