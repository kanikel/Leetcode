class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int

        算法思想：
        1、检查dict是否存在当前的字符，如果存在则更新pointer的位置（到上一次出现的位置的下一个）
        2、计算Max
        3、更新dict （位置很关键，最后才更新dict，也就是）
        
        时间复杂度是O(n),因为从头到尾只走了一遍（每个数只访问了一次）
        巧妙地运用了键值对来解题，将value作为键，因为这道题里面要求value不重复，所以value是唯一的，
        刚好应用了dict的键是唯一的
        """
        
        s_dict = {}
        maxi = 0
        pointer = 0 #左指针
        for index, value in enumerate(s):   #遍历字符串
            if value in s_dict:
                pointer = max(s_dict[value] + 1, pointer)
                #print(pointer)  通过观察这个来明白这种做法的精髓
            maxi = max(index - pointer + 1, maxi)
            s_dict[value] = index
        return maxi