# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m > n or n < 1 or m < 1 or not head.next:
            return head
        cur = head
        l = []
        while(cur):
            l.append(cur.val)
            cur = cur.next
        mid = l[m-1:n]
        mid.reverse()
        r = l[:m-1] + mid + l[n:]
        a = ListNode(0)
        ret = a
        for i in r:
            a.next = ListNode(i)
            a = a.next
        return ret.next