// 最长上升子序列
class Solution {
public:
    /**
     * @param nums: The integer array
     * @return: The length of LIS (longest increasing subsequence)
     */
    int longestIncreasingSubsequence(vector<int> a) {
        // write your code here
        if(a.size() == 0)
            return 0;
        std::vector<int> dp(a.size(), 0);
        dp[0] = 1;
        for(int i = 1; i < a.size(); ++i)
        {
            dp[i] = 1;
            for(int j = 0; j < i; ++j)
            {
                if(a[i] >= a[j] && dp[j] + 1 > dp[i])
                    dp[i] = dp[j] + 1;
            }
        }
        int max = dp[0];
        for(int i = 1;i < dp.size();++i)
            if(max < dp[i])
                max = dp[i];
        return max;
    }
};


