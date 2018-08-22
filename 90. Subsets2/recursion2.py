class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(r, ci, used, cl):    # result, current index, whether pre num is used, current list
            if ci == len(nums):
                r.append(cl[:])
                
            else: 
                helper(r, ci+1, False, cl)
                #cl.append(nums[ci])
                if (used or nums[ci] != nums[ci-1]):    # 如果和之前的一个数不相等（也就是没有duplicates->78）或者前面的数已经取过了的话，那么就可以取，然后把used置为true，表明当前的值取过了，但是假如前一个没取而且后面这个又和前面这个相等的话就不取它，因为这种取得结果是一样的
                    cl.append(nums[ci])
                #f[ci] == True
                    helper(r, ci+1, True, cl)
                    cl.pop()
        
        nums.sort()
        #f = [False] * len(nums)
        r, cl = [], []
        helper(r, 0, True, cl)  # 这里的初始值要选
        return r

# 这种解法和backtrack的思路不相同，