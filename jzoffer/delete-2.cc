/*
struct ListNode {
    int val;
    struct ListNode *next;
    ListNode(int x) :
        val(x), next(NULL) {
    }
};
*/
/*
题目描述

在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
*/
// 注意，此题中重复的元素一个都不保留，所以跟原来的双指针法不同。
class Solution {
public:
    ListNode* deleteDuplication(ListNode* pHead)
    {
        if (pHead == NULL)
            return NULL;

        struct ListNode *p = pHead;
        struct ListNode *q = pHead->next;
        
        struct ListNode *t = NULL;
        pHead = NULL;
        int cnt = 1;
        // 思路：设置p, q 两个节点，对p指向的节点值进行计数。然后q从p的下一个节点之后，进行遍历，统计p指向的
        // 节点值的个数。
        while(q)
        {
            if (p->val == q->val)
            {
                q = q->next;
                cnt += 1;
            }
            else
            {
                // 假如p指向的节点值相同个数为1，则不是重复的，保留到新链表中。
                if (cnt == 1)
                {
                    // 链表投为空和非空，需要分别判断、单独处理.
                    if (pHead == NULL)
                        pHead = t = p;
                    else{
                        t->next = p;
                        t = t->next;
                    }
                    p = q;
                    q = q->next;
                    cnt = 1;
                }
                // 此时，p指向的链表值重复。直接从q 开始下一轮统计。
                else
                {
                    p = q;
                    q = q->next;
                    cnt = 1;
                }
            }
        }
        //假如最后一个数不是重复的，那木q == NULL，这里for循环会跳出。需要单独处理.
        if (cnt == 1)
        {
            if (pHead == NULL)
                pHead = t = p;
            else{
                t->next = p;
                t = t->next;
            }
        }
        //设置链表结束。注意：返回链表可能为空，所以需要判断
        if (t)
            t->next = NULL;
        return pHead;

    }
};
