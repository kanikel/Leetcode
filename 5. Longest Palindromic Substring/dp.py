class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        
        """
        res = ""
        if len(s) == 0 or len(s) == 1:
            return s
        maxi = 0
        dp = [[None] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        #for i in range(len(s)-1):
        #    dp[i][i+1] = s[i] == s[i+1]
        
        for i in range(len(s)):
            for j in range(0, i+1):
                dp[j][i] = s[j] == s[i] and ((i - j <= 2) or dp[j+1][i-1])
                #print j,i
                #print dp[j][i]
                if dp[j][i]:
                    templen = i - j + 1
                    #print(templen)
                    if templen > maxi:
                        res = s[j: i+1]
                        maxi = len(res)
        return res


        
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        
        """
        # brute force will exceed time limit
        """
        brute force will exceed time limit
        so we consider dynamic programming algorithm here, why?
        Because for each substring, we calculate whether it's a palindrome from the beginning to the end everytime
        like abba: a ab b abb bb b abba bba ba a
        
        如果用暴力破解的方法解决这道题，会发现在求解过程中做了很多重复的工作，因为对于每一个子串都需要重头到尾判断是不是回文的。

        回文字符串具有一个性质：当去掉回文字符串的首尾字符后，剩下的子字符串仍然是回文的。反过来利用这个性质，如果我们已经知道了一个子字符串s[i + 1…..j
        - 1]是回文的，那么如果该字符串的前后字符相等，即s[i] == s[j]，就可以直接判断s[i……j]是回文的。

        因此可以用dp[i][j]表示s[i…j]是否回文，1表示是，0表示否。状态转移方程是 
        dp[i + 1][j - 1] == 1且s[i] == s[j]，dp[i][j] = 1； 
        而初始条件有两种情况，分别是单个字符（a）跟两个相同字符（aa），所以初始化dp数组时需要对两种情况都进行初始化。

        从状态转移方程可以看出，计算dp[i][j]时需要用到dp[i+1][j - 1]和dp[i + 1][j]，所以对于i的遍历应该从尾部开始，见下面的动态规划实现。这种算法的
        时间复杂度跟空间复杂度都是O(n^2)，因为每个都是考虑了两遍。
        
        abba
        i=1
        j=2
        """
        if s == "" or len(s) == 0:
            return s
        r = ""
        l = len(s)
        dp = [None]*l
        for i in range(l):
            dp[i] = [None]*l
        #print(dp)
        #dp = [len(s)][len(s)] # it doesn't work like this to create a multi-dim list
        maxi = 0
        for j in range(len(s)):
            for i in range(j+1):
                dp[i][j] = s[i] == s[j] and ((j - i <= 2) or dp[i+1][j-1]) # 假如j-i=1和0的时候就略过dp[i+1][j-1]，因为这个时候的
                #print i, j, dp[i][j]       #dp是之字形在走，而不是按层在走！
                if dp[i][j]:
                    if (j - i + 1 > maxi):
                        maxi = j - i + 1
                        res = s[i:j+1]
        #print(dp)
        return res