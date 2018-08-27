class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #time: O(), space: O(1)
        m = m - 1
        n = n - 1
        return self.fac(m + n) / (self.fac(m) * self.fac(n))
    def fac(self, m):
        if m == 0 or m == 1:
            return 1
        return m * self.fac(m-1)