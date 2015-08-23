/*
struct ListNode {
    int val;
    struct ListNode *next;
    ListNode(int x) :
        val(x), next(NULL) {
    }
};
*/
class Solution {
public:
    ListNode* deleteDuplication(ListNode* pHead)
    {
        if (pHead == NULL)
            return NULL;
        struct ListNode *p = pHead->next;
        struct ListNode *t = pHead;
        t->next = NULL;
        while(p)
        {
            if (t->val == p-val)
                p = p->next;
            else
            {
                t->next = p;
                t = t->next;
                p = p->next;
                t->next = NULL;
            }
        }
        return pHead;

    }
};
