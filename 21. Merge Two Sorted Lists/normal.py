# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = []
        b = ListNode(0)
        c = b
        while l1:
            a.append(l1.val)
            l1 = l1.next
        while l2:
            a.append(l2.val)
            l2 = l2.next
        a.sort()
        for i in a:
            b.next = ListNode(i)
            b = b.next
        return c.next