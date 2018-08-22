class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums : [-2,1,-3,4,-1,2,1,-5,4]
        # f    : [-2,1,-2,4, 3,5,6, 1,5]
        # ans  
        # f[i] denotes the max subarray 0...i
        # 动态规划转移方程： f[i] = f[i-1] > 0 ? nums[i] + f[i-1] : nums[i]
        # 下面这种解法只用了ans一个变量来存储当前的值，所以空间复杂度减小成了O(1)
        s = nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            #ans = 0
            ans = max(nums[i], ans + nums[i])
            s = max(s, ans)
        return s