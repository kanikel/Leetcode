# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        # 赋值好最开始的三个指针的状态
        pre = None
        cur = head
        nex = cur.next
        while (cur != None): # 当前cur不为空的时候：
            cur.next = pre   # cur -> pre
            pre = cur        # pre -> cur
            cur = nex        # cur -> nex
            # 不能直接赋cur = cur.next，因为上面刚赋值，这样等于cur = pre = cur = 1就跳出循环了，所以要按照顺序来，cur
            if cur != None:
                nex = cur.next  # nex -> cur.next = nex.next
            #print pre.val
        return pre           # 只要返回pre就是最新的cur往回指的状态
            