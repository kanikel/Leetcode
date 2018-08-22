class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        
        s = "aabcbababcba"
        
          i     0  1  2  3  4  5  6  7  8  9 10 11 12  13  14 15 16 17 18 19 20 21 22 23 24
                   1     2     3   
        t[i]    #  a  #  a  #  b  #  c  #  b  #  a  #   b   #  a  #  b  #  c  #  b  #  a  #
        p[i]       1  2  1  0  1  0  5  0  1  0  3  0  11   0  3  0  1  0  5  0  1  0  1 
          i     0  1  2  3  4  5  6  7  8  9 10 11 12  13  14 15 16 17 18 19 20 21 22 23 24
                   1     2     3 
        https://www.youtube.com/watch?v=V-sEwsca1ak
        https://www.felix021.com/blog/read.php?2040
        https://articles.leetcode.com/longest-palindromic-substring-part-ii/

        """
        t = "#"
        if len(s) == 0:
            return s
        for i in range(len(s)):
            t += s[i] + "#"
        t += "#"
        # s -> t
        p = [0] * len(t)
        #print(t)
        
        c, b, maxi = 0, 0, 0
        
        res = ""
        
        for i in range(1,len(t)-1):
            im = c - (i - c)
            if b > i:
                if b - i > p[im]:
                    p[i] = p[im]
                else: p[i] = b - i
            else: p[i] = 0
                
            while (i-p[i]) > 0 and (i+p[i]) < len(t) and t[i-p[i]-1] == t[i+p[i]+1]:    #为什么一定要在两边额外加一个#作为sentinal? 因为会报错超出范围，i+p[i]+i会超出范围，事实证明其实在结尾加一个#就好了，不需要两边都加
                p[i] += 1
            #print(i, p[i], c, b)
                
            if (i+p[i]) > b:
                b = i + p[i]
                c = i   # 为什么一定要放在这里？因为不一定更新后的字符串就比原来的大，但是仍然需要更新中心点
                
            if (p[i] > maxi):
                maxi = p[i]
                res = s[(i-maxi)/2 : (i-maxi)/2 + maxi]
                
        return res