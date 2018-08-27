class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #time: O(m*n)
        #space: O(m)
        ret = [0] * m
        ret[0] = 1
        for i in range(0, n):
            for j in range(1, m):
                ret[j] += ret[j-1]
        return ret[m-1]