# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        # Solution 1: uses dict(hashmap) to store the {head : copy}, then traverse the new copy list to update the random pointer
        if head == None:
            return None
        dummy = RandomListNode(0)
        copy = dummy
        d = {}
        h = head
        while h != None:
            dummy.next = RandomListNode(h.label)
            dummy = dummy.next
            d[h] = dummy
            h = h.next
        #copy = copy.next
        ret = copy.next
        newh = head
        copy = copy.next
        while newh != None:
            copy.random = d.get(newh.random)
            copy = copy.next
            newh = newh.next
        return ret