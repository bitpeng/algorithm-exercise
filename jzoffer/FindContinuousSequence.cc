int MySum(int i, int j)
{
    int ret = 0;
    if (i > j)
        return 0;
    for(int begin = i; begin <= j; ++ begin)
        ret += begin;
    return ret;
}
class Solution {
public:
    vector<vector<int> > FindContinuousSequence(int sum) {
        vector<vector<int> > ret;
        vector<int> veci;
        if (tsum < 0)
            return ret;

        int mid = sum / 2 + 1;
        for (int i = 1; i <= mid; ++i)
        {
            j = mid;
            while (i < j)
            {
                int tmp = MySum(i, j);
                if (tmp == sum)
            }
        }
        

    }
};
