import time
t = time.time()
class Solution:
    def FindContinuousSequence(self, n):
        if n <= 0:
            return []

        i = 1; j = 1; sum = 0
        ret = []
        while j < (n / 2 + 2):
            #if sum > n:
            sum += j
            while sum > n:
                    sum -= i
                    i += 1
            if sum == n:
                # ret.append(range(i, j + 1))
                print range(i, j + 1)
            j += 1
        return ret

so = Solution()
print so.FindContinuousSequence(10002001)
print time.time() - t
