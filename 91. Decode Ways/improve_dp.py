class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # bottom-up dynamic programming
        # time: O(n)
        # space: O(1)
        
        if s == None or len(s) == 0 or s[0] == '0':
            return 0
        l = len(s)
        c1 = 1  # c1 is the previous value stored
        c2 = 1  # c2 is the newest value stored

        for i in range(2, l+1):
            
            first = int(s[i-1:i])   
            second = int(s[i-2:i])
            
            if first == 0:
                c2 = 0
                
            if (second >= 10 and second <= 26):
                c2 = c2 + c1    # store the new value into c2
                c1 = c2 - c1    # c1 = c2 + c1 - c1 which is the previous c2
                
            else: c1 = c2       # if second < 10 or second > 26, update c1 to the previous c2
                
        return c2
        
        
        
        