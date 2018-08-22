class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        
        """
        # brute force will exceed time limit
        
        l = len(s)
        max_length = 0
        p = ''      # palindromic
        if len(s) == 1 or len(s) == 0:
            return s
        for i in range(l):
            for j in range(i + 1, l):
                is_p = True
                for k in range(i, int((i+j) / 2) + 1):
                    if s[k] != s[j-k+i]:
                        is_p = False
                        break
                if is_p and (j-i+1) > max_length:
                    max_length = j - i + 1
                    p = s[i:j+1]
        if p == '':
            p = s[0]
        return p