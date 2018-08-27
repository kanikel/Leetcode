class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # time: O(n)
        # space: O(n)
        memo = [None] * n
        def helper(n):
            if memo[n-1]:
                return memo[n-1]
            if n == 1:
                memo[n-1] = 1
                return memo[n-1]
            if n == 2:
                memo[n-1] = 2
                return memo[n-1]
            else: 
                memo[n-1] = helper(n-1) + helper(n-2)
                return memo[n-1]
        return helper(n)