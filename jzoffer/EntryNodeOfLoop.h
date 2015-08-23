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
    ListNode* EntryNodeOfLoop(ListNode* pHead)
    {
        if(pHead == nullptr || pHead->next == nullptr)return nullptr;
        ListNode* pFast = pHead;
        ListNode* pSlow = pHead;
        ListNode* pMeet = nullptr;
        // 假如链表没有环呢，这个循环还能退出么？会造成指针错误。
        // 防御性编程很重要，即函数的正常运行，不能依赖于调用参数(输入数据)的合法性，
        // 而要自己事先注意到，并处理这种情况。
        //while(1)
        while(pFast && pFast->next)
        {
            pSlow = pSlow->next;
            pFast = pFast->next->next;
            if(pFast == pSlow)
            {
                pMeet = pFast;
                break;
            }                 
        }
        if (pMeet == nullptr)
            return nullptr;
        ListNode* pEntrance = pHead;
        while(pEntrance != pMeet)
        {
            pEntrance = pEntrance->next;
            pMeet = pMeet->next;
        }
        return pEntrance;
 
    }
};