class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums)-1
        if nums[left] < nums[right]:
            return nums[left]
        while(left < right):
            mid = left + (right-left)/2
            #print left, right, mid
            if nums[mid] > nums[right]: # 假如是>nums[left]的话无法解决[3,1,2]这种，想下怎么改
                left = mid + 1
            else:
                right = mid
        return nums[left]