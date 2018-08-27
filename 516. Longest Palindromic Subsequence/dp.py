class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        
        The key is to find out the state transaction formula
        
        dp[i][j]: the longest palindromic subsequence's length of substring(i, j), here i, j represent left, right indexes in the string
        State transition:
        dp[i][j] = dp[i+1][j-1] + 2 if s.charAt(i) == s.charAt(j)
        otherwise, dp[i][j] = Math.max(dp[i+1][j], dp[i][j-1])
        Initialization: dp[i][i] = 1
        
        i should start from len(s)-1 to 0 and j should start from i+1 to len(s), outer dp could use inner dp values
        time: O(n^2)
        space: O(n^2)
        """
        
        dp = [[0] * len(s) for i in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else: 
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                    
        return dp[0][len(s)-1]