/*
struct RandomListNode {
    int label;
    struct RandomListNode *next, *random;
    RandomListNode(int x) :
            label(x), next(NULL), random(NULL) {
    }
};
*/
class Solution {
public:
    RandomListNode* Clone(RandomListNode* pHead)
    {
        pHead = CloneNode(pHead);
        pHead = CopyRandomPtr(pHead);
        return SplitList(pHead);
    }

    RandomListNode* CloneNode(RandomListNode* pHead)
    {
        if (pHead == NULL)
            return NULL;
        RandomListNode *p = pHead;
        while(p)
        {
            RandomListNode *tmp = new RandomListNode(p->label);
            tmp->next = p->next;
            p->next = tmp;
            p = tmp->next;
        }
        return pHead;
    }
    RandomListNode* CopyRandomPtr(RandomListNode* pHead)
    {
        if (pHead == NULL)
            return NULL;
        RandomListNode *p = pHead;
        RandomListNode *pNext = pHead->next;
        while(p)
        {
            RandomListNode *pRandomNode = p->random;
            if (pRandomNode != NULL)
                pNext->random = pRandomNode->next;
            //else
            //    pNext->random = NULL;
            p = pNext->next;
            pNext = p->next;
        }
        return pHead;
    }
    RandomListNode* SplitList(RandomListNode* pHead)
    {
        if (pHead == NULL)
            return NULL;
        RandomListNode *p = pHead;
        RandomListNode *pNext = pHead->next;
        RandomListNode *ret = NULL;
        RandomListNode *tail = NULL;
        ret = tail = pNext;

        p->next = pNext->next;
        p = pNext->next;
        //pNext = p->next;
        while(p)
        //while(p && pNext)
        {
            pNext = p->next;
            p->next = pNext->next;

            tail->next = pNext;
            tail = pNext;
            //tail->next = NULL;

            p = pNext->next;
        }
        return ret;

    }
};







