class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        
        recursion backtracking but how?
        
        backtracking:

        time: O(n!)
        space: O(n)

        this solution:
        time: O(n! * n) 
        space: O(n)

        reference: http://www.1point3acres.com/bbs/thread-117602-1-1.html
        
        """
        r,c,s = [], [], []
        if len(nums) == 0:
            return nums
        self.helper(r, nums, c, s) # input arguments: result input_nums currentlist set
        return r
    
    def helper(self, r, nums, c, s):
        if len(c) == len(nums):
            r.append(c[:]) # ？？？？？？？！！！！！！！！！！！赋值的时候特别小心啊！！
            # r.append(c) != r.append(c[:]) !!! 后者是通过切片把c复制了一份新的，而前者是指向了c的一个名字，所以最后是会变成[[]]，因为最后c变成了[]
            #print c
        else:
            for i in range(len(nums)):
                if not s.count(nums[i]):    # O(n)
                    c.append(nums[i])
                    s.append(nums[i])
                    #print i, c
                    last = len(c) - 1
                    #print "before", i, c
                    self.helper(r, nums, c, s)
                    #print "after", i, c
                    c.remove(c[last])
                    s.remove(s[last])