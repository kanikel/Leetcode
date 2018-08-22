class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 这道题用的是动态规划DP的思想，要看花花画的那个流程你才能弄懂
        dp = [0] * (target + 1) # 初始化全为0， 默认没有解
        dp[0] = 1       # dp[i] : of combinations sum up to i; 0的情况就是{}
        for i in range(1, target+1):    # 把比target小的所有情况都给计算一遍
            for num in nums:
                if i - num >= 0:        # i - num >= 0的时候就把子问题加入，相当于target >= nums[i]
                    dp[i] += dp[i - num]    # i-num等于子问题的个数，递归的思想在这里也用到
                    #print i, i-num
        return dp[target]
