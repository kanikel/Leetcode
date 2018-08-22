class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        s1 = []
        if s == "":
            return 0
        temp = 0
        maxi = 1
        s2 = set(s)
        for i in xrange(len(s)):
            s1.append(s[i])
            j = i+1
            if temp>maxi:
                maxi = temp
            for j in xrange(j,len(s)):
                if s1.count(s[j]):
                    #temp = len(s1)
                    s1=[]
                    break
                else: 
                    s1.append(s[j])
                    temp = len(s1)
                    
        
        return maxi
            
# it is a O(n2) solution and it can't work out for the super long string input