class Solution {
    int findmin(vector<int> &v, int low ,int high){
    int res=v[low];
    for(int i=low+1;i<=high;i++){
        if(v[i]<res) res=v[i];
    }
        return res;
    }
public:
    int minNumberInRotateArray(vector<int> rotateArray) {
    if (rotateArray.size() <= 0)
        return 0;
    int begin = 0, end = rotateArray.size() - 1;
    int middle = 0;
    while (rotateArray[begin]>=rotateArray[end])
    {
         
        if (end - begin == 1)
        {
            middle = end;
            break;
        }
        middle = (begin + end) / 2;
        if(rotateArray[middle]==rotateArray[begin] && rotateArray[middle]==rotateArray[end])
        {
            return findmin(rotateArray, begin , end);
        }
             
             
         
        if (rotateArray[middle]>=rotateArray[begin])
            begin = middle;
        if (rotateArray[middle]<=rotateArray[end])
            end = middle;
    }
    return rotateArray[middle];
    }
};