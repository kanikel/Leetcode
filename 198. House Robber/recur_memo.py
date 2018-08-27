class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # time: O(n)
        # space: O(n)
        
        l = len(nums)
        memo = [-1] * l
        return self.helper(nums, l - 1, memo)
    
    def helper(self, nums, i, memo):
        if i < 0:
            return 0    # padding all the values to 0 if i < 0
        if memo[i] >= 0:
            return memo[i]
        memo[i] = max(self.helper(nums, i-2, memo) + nums[i], self.helper(nums, i-1, memo))
        #print memo[i]
        return memo[i]