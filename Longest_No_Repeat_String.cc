#include <cstdio>
#include <cstring>

int main()
{
    char s[10001];
    while(scanf("%s", s) != EOF)
    {
        int p[128]; //保存s中每一个字符最近一次出现的位置
        for (char c = 'a'; c <= 'z'; ++c)
        {
            p[c] = -1;
        }

        int n = strlen(s), right = -1, answer(0);  //right保存出现重复字符时重复字符的上一个位置
        for (int i = 0; i < n; ++i)
        {
            if (p[s[i]] > right) //每一字符上一次出现的位置 > right
            {
                right = p[s[i]];
            }
            p[s[i]] = i;

            if (i - right > answer)
            {
                answer = i - right;
            }
        }

        printf("%d\n", answer);
    }

    return 0;
}
