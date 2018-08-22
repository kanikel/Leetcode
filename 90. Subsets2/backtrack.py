class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(r, ci, l): # current result, current index, current list, used flag
            r.append(l[:])
            
            for i in range(ci, len(nums)):
                if (i > ci and nums[i] == nums[i-1]): continue # 和79的区别就在于这一语句，也就是从上一个数的下一个开始，也就保证了一个和前面相同的数最多取一次，不会超过一次
                l.append(nums[i])
                backtrack(r, i+1, l)
                l.pop()
                
        r, l = [], []
        nums.sort()
        backtrack(r, 0, l)
        return r
                
        