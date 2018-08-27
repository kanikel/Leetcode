class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        tail = [nums[0]]
        s = 0               # start
        e = 0               # end 
        for num in nums:
            if tail[e] < num:
                tail.append(num)
                e = len(tail) - 1
                print tail
                continue
            while (s != e):
                m = s + (e - s)/2
                if tail[m] > num:
                    e = m
                elif tail[m] < num:
                    s = m + 1
                else: break
            tail[s] = num
            e = len(tail) - 1
            print tail
        return len(tail)