class Solution {
public:
    /*
     * param k : description of k
     * param nums : description of array and index 0 ~ n-1
     * return: description of return
     */
    int kthLargestElement(int k, vector<int> nums) {
        // write your code here
        if(k <= 0 || k > nums.size())return -1;
        return partion(nums, 0, nums.size() - 1, k);
    }
    int partion(vector<int> &nums, int b, int e, int k)   // [b, e]
    {
        if(b >= e || k <= 0)return nums[b];
        int i = b;
        for(int j = b + 1;j <= e;++j)
        {
            if (nums[j] >= nums[b])
            {
                i++;
                swap(nums[i], nums[j]);
            }
        }
        swap(nums[b], nums[i]);
        if(i - b + 1 == k)
            return nums[i];
        else if(i - b + 1 > k)
            return partion(nums, b, i  , k);
        else
            return partion(nums, i + 1, e, k - (i - b + 1));
    }
    void swap(int &a, int &b)
    {
        int tmp = a;
        a = b;
        b = tmp;
    }
};

