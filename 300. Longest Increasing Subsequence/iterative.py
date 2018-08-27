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
        dp[0] = 1
        for i in xrange(1, n):
            count, tmp, maxi = 0, 0, 0  # one to store the count, one to store the current value, one to store the max value
            for j in xrange(0, i):
                if nums[i] > nums[j]:
                    tmp = dp[j] + 1
                    if tmp > maxi:
                        maxi = tmp
                        dp[i] = maxi
                else:
                    count += 1
                    if count == i:
                        dp[i] = 1
        #print dp
        return max(dp)