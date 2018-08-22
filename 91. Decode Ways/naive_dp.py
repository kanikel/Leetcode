class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # bottom-up dynamic programming
        # time: O(n)
        # space: O(n)
        
        if s == None or len(s) == 0:
            return 0
        l = len(s)
        dp = [0] * (l + 1)  # it requires an addiitonal space for the empty string
        dp[0] = 1   # we set the empty string has 1 way because dp stores its value 1 index ahead
        dp[1] = 1 if s[0] != '0' else 0 # deal with the first value
        for i in range(2, l + 1):   # range from 0 to l (l + 1)
            first = int(s[i-1:i])   # turn the first character into integer
            second = int(s[i-2:i])  # turn the first two characters into integer
            if first >= 1 and first <= 9:
                dp[i] += dp[i-1]    # deal with the value start from the index 1 
            if second >= 10 and second <= 26:
                dp[i] += dp[i-2]    # deal with the value start from 01, 12, 23...
        return dp[l]    # return the corresponding dp