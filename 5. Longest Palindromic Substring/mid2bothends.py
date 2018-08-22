class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        
        """
        res = ""
        if s == "" or len(s) == 0:
            return s
        for i in xrange(len(s)):
            res = self.helper(s, i, i, res)    # aba
            res = self.helper(s, i, i+1, res)  # abba
        return res
    
    def helper(self, s, left, right, res):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        cur = s[left+1 : right]
        if (len(cur) > len(res)):
            res = cur
        return res # 为什么这里是值调用呢，因为这里的res是str，str是不能更改内容的，所以要把值返回去，可以参考这篇博文
        #https://www.techforgeek.info/python_pass_para_by_reference.html
            