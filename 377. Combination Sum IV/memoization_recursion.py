class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        memo = [-1] * (target+1)
        memo[0] = 1
        
        def dp(nums, target):
            if target < 0: return 0
            if memo[target] != -1: return memo[target]
            ans = 0
            for num in nums:    
                ans += dp(nums, target - num)
                #memo[target] = 0
                #memo[target] += dp(nums, target-num)              
                memo[target] = ans      #这里还是没有搞懂为什么需要一个ans来存储
            return ans
                                
        return dp(nums, target)
        #return r[target]