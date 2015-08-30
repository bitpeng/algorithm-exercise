import random
import time

t = time.time()
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

print LongestRepeatSubstring("abcdefcdef")
print LongestRepeatSubstring("abcdefcdefc")
print LongestRepeatSubstring("abcdefcdefcd")
s = ''.join([chr(random.randint(97, 105)) for i in range(5000)])
#print s
print LongestRepeatSubstring(s)
print time.time() - t
