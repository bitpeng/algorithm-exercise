#define N 128
/**
    求最长不重复子串的线性算法！
    分析：比如字符串 s = "abcdefgechijklmng"
    1. 扫描过"abcdefg"，此时max = 7; lastRepeat = -1;
    2. 扫描到e, 此时出现重复字符，因此更新lastRepeat = 4;
    3. 在循环体中，tmp = i - lastRepeat这里我的想法是是从上一个不重复的子串进行计算,
       但是我没有考虑到，s[i]可能和lastRepeat之后的某个字符重复.比如, 最后一个g和第
       g重复, 因此我还是从第一个e计算，肯定错了。
    4. lastRepeat = a[s[i]], 这里想保存出现重复字符时重复字符的上一个位置,从这里开始
       计算，但是重新出现重复字符的位置可能在lastRepeat左边，比如第二个c, 它在lastRepeat
       ( 此时指向第一个e)，那么这里不应该更新lastRepeat.
    5. 指出了这两点问题，程序就很好改正了.
*/
// 这个程序有问题，请看上面的分析！
int LongestNoRepeatSubstring_Wrong(char s[])
{
    int n = strlen(s);
    int lastRepeat = -1; // 出现重复字符时重复字符的上一个最右边位置！
    int a[N] = 128;
    int max = 0;
    for(int i = 0;i < N;++i)
        a[i] = -1;
    for(int i = 0;i < n;++i)
    {
        tmp = i - lastRepeat;
        lastRepeat = a[s[i]];
        a[s[i]] = i;
        if(tmp > max) max = tmp;
    }
}
// 更正过的版本
int LongestNoRepeatSubstring_Right(char s[])
{
    int n = strlen(s);
    int lastRepeat = -1; // 出现重复字符时重复字符的上一个最右边位置！
    int a[N] = 128;
    int max = 0;
    for(int i = 0;i < N;++i)
        a[i] = -1;
    for(int i = 0;i < n;++i)
    {
        //tmp = i - lastRepeat;
        if (a[s[i]] > lastRepeat)  //只有出现重复字符时，他的上一个位置在lastRepeat
            lastRepeat = a[s[i]];  //左边才更新, 比如第二个c, 它就不进行更新
        a[s[i]] = i;
        tmp = i - lastRepeat
        if(tmp > max) max = tmp;
    }
}
