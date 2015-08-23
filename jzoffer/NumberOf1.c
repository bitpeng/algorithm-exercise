class Solution {
public:
     int NumberOf1(int n) {
	 if(n == 0)
		return 0;
         int sum = 1;
         int x = n;
         while (x & (x - 1))
         {
             sum += 1;
             x = x & (x - 1);
         }
         return sum;
         
     }
};
