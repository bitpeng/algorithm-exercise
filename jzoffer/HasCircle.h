/** 
 * judge the list has circle or not 
 */  
template <typename Type>  
bool HasCircle(ListNode<Type> *head)  
{  
    if(head == NULL)  
        return false;  
  
    ListNode<Type> *fast, *slow;  
    fast = slow = head;  
  
    while (fast && fast->next != NULL)  
    {  
        fast = fast->next->next;  
        slow = slow->next;  
  
        if(fast == slow)  
            return true;  
    }  
  
    return false;  
}  