class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        r,c, flag = [], [], [False] * len(nums)
        
        nums.sort() #必须排序过，才能保证前一个情形就把现在的给包含进去了
        
        if len(nums) == 0:
            return [[]]
        self.helper(r, flag, c, nums) # input arguments: result flag currentlist input_nums
        return r
    
    def helper(self, r, flag, c, nums):
        if len(c) == len(nums):
            r.append(c[:])
        else:
            for i in range(len(nums)):
                if flag[i]: continue    # 假如之前都用过了，那么跳过if i > 0 and nums[i] == nums[i-1] and flag[i-1]: continue
                 # 如果当前值和前一个相同，且前一个值已经用过了，那么也要跳过，而且当i=0的时候这个值不能跳过，所以要加上i>0的情形
                c.append(nums[i])
                #print i, c
                flag[i] = True
                self.helper(r, flag, c, nums)
                flag[i] = False
                c.pop()