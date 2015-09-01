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



int main()
{
    printf("%c\n", FirstNoRepeatChar("hello, world"));
    Test_DeleteCharInStr2();
    Test_Ptr_Arr();
    return 0;
}
