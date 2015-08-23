#include <stack>
#include <vector>
using namespace std;
class Solution {
public:
    bool IsPopOrder(vector<int> pushV,vector<int> popV) {
        if(pushV.empty() || popV.empty())
            return false;
        stack<int> s;
        size_t k = 0;
        for(size_t i = 0; i != pushV.size(); ++i) {
            s.push(pushV[i]); /* 1 2 3 4 5 入栈 */      
            while(!s.empty() && popV[k] == s.top()) {  
                k++;
                s.pop();
            }
        }
          
        if(s.empty()) {
            return true;
        } else {
            return false;
        }
    }
};