/*
struct ListNode {
    int val;
    struct ListNode *next;
    ListNode(int x) :
            val(x), next(NULL) {
    }
};*/
class Solution {
public:
    ListNode* FindFirstCommonNode( ListNode *pHead1, ListNode *pHead2) {
        if (pHead1 == NULL || pHead2 == NULL)
            return NULL;
        int len1 = ListLength(pHead1);
        int len2 = ListLength(pHead2);
        if (len1 > len2)
        {
            ListNode* tmp = pHead1;
            pHead1 = pHead2;
            pHead2 = tmp;
            int t = len1;
            len1 = len2;
            len2 = t;
        }
        ListNode* p1 = pHead1,*p2 = pHead2;
        for (int i = 0;i < len2 - len1; ++i)
        {
            p2 = p2->next;
        }
        while (p1 != p2 && p1 && p2)
        {
            p1 = p1->next;
            p2 = p2->next;
        }
        if (p1 == NULL || p2 == NULL)
            return NULL;
        return p1;       
        
    }
    int ListLength(ListNode* p)
    {
        // if (p == NULL)
            // return 0;
        int k = 0;
        while(p)
        {
            ++k;
            p = p->next;
        }
        return k;
    }
};