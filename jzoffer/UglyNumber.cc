class Solution {
public:
    int GetUglyNumber_Solution(int index) {
        if (index < 1)
            return -1;
        switch(index){
            case 1:
                return 1;
            case 2:
                return 2;
            case 3:
                return 3;
            case 4:
                return 4;
            case 5:
                return 5;
        }
        int *a = new int[index];
        for (int i = 0;i < 5;++)
            a[i] = i + 1;
        int num = 6; //从6开始，依次判断每一个数是否是丑数。
        int i = 5;   //下一个丑数保存位置下标
        for(;true;)
        {
            int j = 0;
            for (;a[j] * a[j] <= num;++j)
                NULL;
            //for (int j = i;a[j] * a[j] <= num ; ++j)
            for (;j >= 0; ++j)
            {
                if(num % a[j] == 0)
                    num /= a[j];
                if (a[j] <= 5)
                    




            }
        }

    }
};
