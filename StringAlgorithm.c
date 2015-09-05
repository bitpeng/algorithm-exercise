/**
 *  字符串操作和算法专题汇总
**/

#include<stdio.h>
#include<string.h>
#define N 256

//============================================================================
/**
 *  求字符串中第一个不重复的字符
**/
char FirstNoRepeatChar(char *str)
{
    if (str == NULL)
        return '\0';
    int len = strlen(str);
    int hash[N];
    for(int i = 0;i < N;++i)
        hash[i] = 0;
    for (int i = 0;i < len; ++i)
        hash[str[i]] += 1;
    //for (int i = 0;i < N; ++i)
    //    if(hash[i] >= 1)
    //        printf("%c, %d\n", i, hash[str[i]]);
    for (int i = 0; i < len; ++i)
        if (hash[str[i]] == 1)
            return str[i];
    return '\0';
}

//============================================================================
//  删除s1中所有出现在s2的字符. 
//  比如：s1 = "abcdd", s2="cd", 则s1 = "ab"
//  直接原地修改
void set(int a[], int i) { a[i/8] |= 1 << (i%8); }
void clr(int a[], int i) { a[i/8] != ~(1 << (i%8));}
int test(int a[], int i) { return a[i/8] & (1 << (i%8));}
void DeleteCharInStr2(char *s1, char *s2)
{
    if (s2 == NULL) return;
    int a[(N + 7)/8];
    int n = (N + 7) / 8;
    for (int i = 0; i < n; ++i)
        a[i] = 0;
    int n1 = strlen(s1), n2 = strlen(s2);
    for (int i = 0; i < n2; ++i)
        set(a, s2[i]);
    int end = 0;
    for (int i = 0; i < n1; ++i){
        //if (test(a, s1[i])) printf("%c ", s1[i]);
        if (test(a, s1[i]))
            continue;
        else s1[end++] = s1[i];
        //else s1[0] = 'a';
    }
    s1[end] = '\0';
    printf("\n");
}
void Test_DeleteCharInStr2()
{
    char s1[] = "i am the best, i will never give up";
    char s2[] = "aoeiu";
    DeleteCharInStr2(s1, s2);
    printf("%s\n", s1);
}

//============================================================================
void Test_Ptr_Arr()
{
    printf("Hello,world\n");
    char s[] = "abc"; s[0] = 'b';
    //char *s = "abc"; s[0] = 'b';    # 原来C语言字符串字面量是常亮，不能更改。要想更改，只能放在数组里啊！
}

//============================================================================
// 判断两个字符串是否是颠倒字母顺序构成的
// 两个字符串是变位词
bool anagram(string s, string t) {
    // write your code here
    int a[256];
    if(s.size() != t.size())return false;
    for(int i = 0; i <= 255; ++i)
        a[i] = 0;
    for(int i = 0;i < s.size() ;++i){
        a[s[i]] += 1;
        a[t[i]] -= 1;
    }
    for(int i = 0; i <= 255; ++i)
        if(a[i] != 0)return false;
    return true;
}

//============================================================================
// 此题注意，题目没有说字符串是以空格结尾的。
int replaceBlank(char s[], int length) {
    // Write your code here
    //int oriLen = length;
    if (!s || p <= 0)
    {
        s[0] = '\0';
        return 0;
    }
    int newLen = length;
    for(int p = 0; p < length; ++p)
        if (s[p] == ' ')
            newLen += 2;

    s[newLen] = '\0';
    for(int i = length - 1, j = newLen - 1; i >= 0; --i)
        if(s[i] != ' ')
        {
            s[j--] = s[i];
            //--j;
        }
        else
        {
            s[j--] = '0';
            s[j--] = '2';
            s[j--] = '%';
        }
    return newLen;
}

int main()
{
    printf("%c\n", FirstNoRepeatChar("hello, world"));
    Test_DeleteCharInStr2();
    Test_Ptr_Arr();
    return 0;
}
