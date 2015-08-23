class Solution {
public:
    bool VerifySquenceOfBST(vector<int> s) {
        if (s.size() == 0)
            return false;
        return check(s, 0, s.size() - 1);
    }
    
    bool check(vector<int> &s, int begin, int end) // 检查下标[begin,end] 之间的序列是不是
    {
        if (end - begin <= 1)
            return true;
        int root = s[end];
        int i,j ;
        // 左子树的下标范围为[begin, i - 1] ,可能为空, 为空时i == begin.
        for(i = begin; i <= end - 1; )
            if (s[i] <= root)
                i++;
            else
                break;
        j = i;
        // 由子树的下标范围为[i, end - 1]，可能为空, 为空时i == end 
        for(;j <= end - 1;)
            if (s[j] >= root)
                j++;
            else 
                return false;
        if (i == begin || i > end - 1)
            return check(s, begin, end - 1);
        //else if (i > end - 1)        
        else
            return check(s,begin,i - 1) && check(s,i ,end);
        
    }
};