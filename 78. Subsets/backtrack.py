class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(r, ci, cl): # current result, current index, current list
            r.append(cl[:])
            #print ci, cl
            
            for i in range(ci, len(nums)):    
                    cl.append(nums[i])
                    backtrack(r, i+1, cl)   #这里是i+1，不是ci+1，要把最新的index作为起始的index，不然会出现重复元素，如[1,3,3]
                    #print i, ci
                    cl.pop()
        
        r, cl = [], []
        backtrack(r, 0, cl)
        return r