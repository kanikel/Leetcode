class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        r,c = [], []
        if len(nums) == 0:
            return [[]]
        self.helper(r, 0, nums) # input arguments: result input_nums currentlist set
        return r
    
    def helper(self, r, start, nums):
        if start == len(nums):
            r.append(nums[:])  # deep copy
            print "inside", nums
        else:
            for i in range(start, len(nums)):
                self.swap(nums, start, i)
                #print i, start, "before", nums # to help you figure out how the recursion works
                self.helper(r, start+1, nums)   # recursion
                self.swap(nums, start, i)       
                #print i, start, "after", nums  # to help you figure out how the recursion works
    
    def swap(self, nums, left, right):
        temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp