class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Use recursion and memoizaiton to rewrite dp
        # time: O(n^2)
        # space: O(n^2)
        memo = [[None] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            memo[i][i] = 1
        return self.helper(s, 0, len(s)-1, memo)
        
    def helper(self, s, i, j, memo):
        if memo[i][j]:
            return memo[i][j]
        if i > j: return 0
        if i == j: return 1
        if s[i] == s[j]:
            memo[i][j] = self.helper(s, i+1, j-1, memo) + 2
        else:
            memo[i][j] = max(self.helper(s, i+1, j, memo), self.helper(s, i, j-1, memo))
        return memo[i][j]
        