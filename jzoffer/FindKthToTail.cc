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
    ListNode* FindKthToTail(ListNode* pListHead, unsigned int k) {
        unsigned int n = 1;
        ListNode *p2 = pListHead;
        ListNode *p1 = pListHead;
        while(n <= k && p2)
        {
            p2 = p2->next;
            ++n;
        }
        if (!p2)return NULL;
        while(p2)
        {
            // if (!p1)
                // p1 = pListHead;
            // else
                // p1 = p1->next;
            p2 = p2->next;
        }
        return p1;

    }
};

