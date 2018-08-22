class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def recursion(r, ci, cl): # current result, current index, current list
            if ci == len(nums):
                r.append(cl[:])
            else:
                recursion(r, ci+1, cl)
                cl.append(nums[ci])
                recursion(r, ci+1, cl)   # 根本不需要用for循环，因为这里调用的时候是加1调用，这也是一个递归不需要用到循环的很好的例子，因为本身就是循环的思想
                cl.pop()
        
        r, cl = [], []
        recursion(r, 0, cl)
        return r