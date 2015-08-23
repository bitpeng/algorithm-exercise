#coding:utf-8
'''
 * Implement the following operations of a stack using queues.
 * 
 * push(x) -- Push element x onto stack.
 * pop() -- Removes the element on top of the stack.
 * top() -- Get the top element.
 * empty() -- Return whether the stack is empty.
 * Notes:
 * You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
 * Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
 * You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
 * Update (2015-06-11):
 * The class name of the Java function had been updated to MyStack instead of Stack.
 * 
 * Credits:
 * Special thanks to @jianchao.li.fighter for adding this problem and all test cases.
'''

## 特别注意这里，不能使用Queue，这个队列是在多线程里交换数据的。
#from Queue import Queue
#
#class Stack
#    q1 = Queue()
#    q2 = Queue()
#    q1_used = True
#    q2_used = False
#
#    # initialize your data structure here.
#    def __init__(self):
#        pass 
#
#    # @param x, an integer
#    # @return nothing
#    def push(self, x):
#        if q1_used:
#            self.q1.put(x)
#        else:
#            self.q2.put(x)
#
#    # @return nothing
#    def pop(self):
#        if self.empty():
#            return
#
#        if self.q1_used:
#            while(self.q1.qsize() > 1):
#                tmp = self.q1.get()
#                self.q2.put(tmp)
#
#
#
#    # @return an integer
#    def top(self):
#        
#
#    # @return an boolean
#    def empty(self):
#        return self.q1.qsize() >=1 or self.q2.qsize() >=1




from collections import deque

class Stack:
    q1 = deque()
    q2 = deque()
    q1_used = True
    q2_used = False

    # initialize your data structure here.
    def __init__(self):
        pass 

    # @param x, an integer
    # @return nothing
    def push(self, x):
        if self.q1_used:
            self.q1.append(x)
        else:
            self.q2.append(x)

    # @return nothing
    def pop(self):
        if self.empty():
            return

        if self.q1_used:
            while(len(self.q1) > 1):
                tmp = self.q1.popleft()
                self.q2.append(tmp)
            self.q1.popleft()
            self.q1_used = False
            self.q2_used = True
        else:
            while(len(self.q2) > 1):
                tmp = self.q2.popleft()
                self.q1.append(tmp)
            self.q2.popleft()
            self.q2_used = False
            self.q1_used = True


    # @return an integer
    def top(self):
        if self.q1_used:
            return self.q1[0]
        else:
            return self.q2[0]

    # @return an boolean
    def empty(self):
        return len(self.q1) == 0 and len(self.q2) == 0


s = Stack()
s.push(1)
print s.pop()
print s.empty()
