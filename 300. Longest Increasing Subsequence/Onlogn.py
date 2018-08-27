class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
          
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i < j:        # i != j is also fine
                # m = (i + j) / 2
                m = i + (j - i)/2
                # print "m:", m
                if tails[m] < x:
                    i = m + 1   # i equals to m+1, which means if x > tails[end], then i becomes j
                else:
                    j = m
            tails[i] = x
            #print " i:",i, " size:",size," tails:",tails
            size = max(i + 1, size)     # if i = j (which means we add a value in the tail), then size = size + 1
        return size