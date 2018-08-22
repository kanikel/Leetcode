class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        r,c, flag = [], [], [False] * len(nums)
        
        nums.sort() # 必须先sort一遍
        #print(nums)
        
        if len(nums) == 0:
            return [[]]
        self.helper(r, flag, c, nums) # input arguments: result flag currentlist input_nums
        return r
    
    def helper(self, r, flag, c, nums):
        if len(c) == len(nums):
            r.append(c[:])
        else:
            prenum = nums[0] - 1
            for i in range(len(nums)):
                if flag[i] == False and nums[i] != prenum:  # 加多了一个判断语句，当前的值不仅不能用过，还不能和上一个数字相同，感觉这样写不太容易明白
                    prenum = nums[i]
                    c.append(nums[i])
                    print i, prenum, c
                    flag[i] = True
                    self.helper(r, flag, c, nums)
                    flag[i] = False
                    c.pop()
        