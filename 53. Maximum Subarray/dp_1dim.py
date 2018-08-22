class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums : [-2,1,-3,4,-1,2,1,-5,4]
        # f    : [-2,1,-2,4, 3,5,6, 1,5]
        # f[i] denotes the max subarray 0...i
        # 动态规划转移方程： f[i] = f[i-1] > 0 ? nums[i] + f[i-1] : nums[i]
        # 因为新开辟的空间大小和nums的一样，然后每个元素都会遍历一遍，所以这种解法是O(n)的时间复杂度和O(n)的空间复杂度
        
        f = [0] * len(nums)
        f[0] = nums[0]
        for i in range(1, len(nums)):
            if f[i-1] > 0:
                f[i] = f[i-1] + nums[i]
            else:
                f[i] = nums[i]
        return max(f)