class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # time: O(n^2), space: O(1)
        # Brute Force, TLE
        maxi = -pow(2,31)
        l = len(nums)
        for i in xrange(0, l):
            p = 1
            for k in xrange(0, l-i):
                p *= nums[i+k]
                #print p
                if p > maxi:
                    maxi = p
        return maxi