class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # LIS(i) = lIS(i-k) + 1 if nums[i] > nums[i-k]
        # time: O(n^2)
        # space: O(n)
        
        if not nums:
            return 0
        n = len(nums)
        dp = [0] * n
        ret = 1 # so that when n == 1, ret is 1
        for i in xrange(0, n):
            dp[i] = 1           # set the dp value to 1 since the shortest len is 1
            for j in xrange(0, i):
                if nums[i] > nums[j] and dp[j] + 1 > dp[i]: 
                    # these two conditions are very important, which can store the largest value of dp[i] in its right place
                    dp[i] = dp[j] + 1
                    if dp[i] > ret:
                        ret = dp[i] # use ret to store the longest length till now
                        #print i, ret
        #print dp
        return ret
                    
            