class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # time:  O(log(n))
        # space: O(n)
        def helper(nums, l, r):
            if nums[l] < nums[r]:
                return nums[l]      # 时间复杂度是O(1)
            if r - l <= 1:          # 用于处理最终分到两个最小的情况
                return min(nums[l], nums[r])
            mid = l + (r - l)/2     # (r + l)/2 may overflow if r or l reaches 2^31
            
            return min(helper(nums, l, mid-1), helper(nums, mid, r))    # 这道题就是发现了规律所以使用递归，也就是一定有一半是排过序的，这样总的复杂度就会从O(n)降到O(logn)(worst case)，平均时间复杂度还要比这个小
        
        l = 0
        r = len(nums) - 1
        return helper(nums, l, r)