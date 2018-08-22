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
        # Solution 2: uses recursion to copy the list and update the random
        
        def copyrandomlist(head):
            if head == None:
                return None
            copy = d.get(head)  # use dict(hashmap) to store the list <-> copy list
            if copy == None:
                copy = RandomListNode(head.label)
                d[head] = copy
                copy.next = copyrandomlist(head.next)
                copy.random = copyrandomlist(head.random)
            return copy
        
        d = {}
        ret = copyrandomlist(head)
        return ret