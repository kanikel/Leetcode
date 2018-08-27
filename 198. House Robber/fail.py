class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = [None] * len(nums)
        return self.helper(nums, memo)
    
    def helper(self, nums, memo):
        n = len(nums) - 1
        if memo[n]:
            return memo[n]
        elif len(nums) == 0:
            return 0
        elif len(nums) == 1:
            memo[0] = nums[1]
            return memo[1]
        elif len(nums) == 2:
            memo[1] = max(nums[0], nums[1])
            return memo[2]
        elif len(nums) == 3:
            memo[2] = max(nums[1], nums[0] + nums[2])
        else:
            memo[n] = max((self.helper(nums[0:-2]+ nums[-1], memo), self.helper(nums[0:-1], memo))
            return memo[n]
        