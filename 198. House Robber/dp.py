class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # time: O(n)
        # space: O(n)
        
        if not nums:
            return 0
        dp = [0] * len(nums)
        for i in xrange(0, len(nums)):
            
            dp[i] = max(dp[i-2] + nums[i] if i > 1 else nums[i], dp[i-1] if i > 0 else 0)
            
        return dp[-1]