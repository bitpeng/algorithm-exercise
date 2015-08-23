struct ListNode {
    int val;
    struct ListNode *next;
    ListNode(int x) :
            val(x), next(NULL) {
    }
};

class Solution {
public:
    ListNode* Merge(ListNode* pHead1, ListNode* pHead2)
    {
        if (NULL == pHead1 || NULL == pHead2)
        {
            if (pHead1)
                return pHead1;
            else if (pHead2)
                return pHead2;
            else return NULL;
        }
        ListNode *ret = NULL;
        ListNode *tail = NULL;
        ListNode *p1 = pHead1;
        ListNode *p2 = pHead2;
        //ret = tail = (p1->next <= p2->next?p1:p2)
        if (p1->val <= p2->val)
        {
            ret = tail = p1;
            p1 = p1->next;
        }
        else
        {
            ret = tail = p2;
            p2 = p2->next;
        }
        while(p1 && p2)
        {
            if (p1->val <= p2->val)
            {
                tail->next = p1;
                p1 = p1->next;
            }
            else
            {
                tail->next = p2;
                p2 = p2->next;
            }
            tail = tail->next;
        }
        tail->next = p1?p1:p2;
        return ret;

    }
};
