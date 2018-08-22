# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        r,p = ListNode(0), ListNode(0)
        r = p # linked list走过一个节点指针就会变到后面去，所以这里要绑定r和p，p是没有走过的，所以指针没有移到下一个
        s = 0
        while l1 or l2:
            if l1:              #这里分开加if是因为两个数的长度可能不同！
                s += l1.val     #一定要动脑子！
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next
            r.next = ListNode(s%10)
            s/=10
            r = r.next
        if s == 1:  # 有可能最后一位还有进位，放在上面的while里面效果相同
            r.next = ListNode(s)
        return p.next # 因为p的当前位是0