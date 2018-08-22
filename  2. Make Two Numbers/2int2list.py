# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2): #在python3里面 /= 会精确到小数点后面
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def toint(l): #这种写法相当于是定义了私有函数toint和tolist
            s = 0
            s += l.val
            if l.next:
                s += 10*toint(l.next)
            return s
        
        def tolist(s):
            a = ListNode(s%10)
            b = a
            while s>9: #假如仅仅是大于0的话会多算一位
                s/=10
                a.next = ListNode(s%10)
                a = a.next
            return b
        
        return tolist(toint(l1) + toint(l2))