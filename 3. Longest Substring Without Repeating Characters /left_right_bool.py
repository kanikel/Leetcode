class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
		
		从Java代码改写过来的

		记住：好的coder想的是data structures和算法，而非code itself!

        算法思想：
        1、用一个128维大小的来存储character是否被用过，常用的char的ascii码的范围长度为128
        2、用right指针来记录是否用到，如果之前没用到就置为true，如果之前用到就计算长度，
        并且假如是和left相同的就两个同时后移一位，假如不同意味着是right遇到和中间字符串下相同的。
        这个时候就把left移动到这一字符的下一个，并且把从left到当前字符全部置回false，因为后面
        还可能用到这跳过的几个字符来组成更长的串
        3、最后出来的时候还要比较一次maxi和当前right-left，取最大值，因为在right后面没遇到用过的
        但此时结束循环的时候没有计算过right-left的值，等于漏了最后一次

        """
        if not s or len(s) == 0:
            return 0
        left , right = 0, 0
        n = len(s)
        flag = [False] * 128 #用一个128维大小的来存储characters，起到的作用和dict相似
        #print(flag)
        maxi = 1
        while right < n:
            if flag[ord(s[right])] == False:
                flag[ord(s[right])] = True # SB写成了==导致看了1个小时
                right += 1
                #print(right)
                #print(ord('z'))
            else:
                maxi = max(maxi, right - left)
                #print('maxi=',maxi)
                while (left < right and s[right] != s[left]):
                    flag[ord(s[left])] = False
                    #print(left)
                    left += 1
                    #print(left)
                left += 1
                #print(left)
                right += 1
        maxi = max(maxi, right - left)
        return maxi