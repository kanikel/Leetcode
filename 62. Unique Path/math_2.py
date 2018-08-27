class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #time: O(m) or O(n), space: O(1)
        # C_m_n = m! / n! * (m-n)!
        # C_m_n = (m - n + 1) * (m - n + 2) * ... * m / n!
        ret = 1.0
        M = m + n - 2
        N = m - 1
        for i in xrange(1, N+1):
            ret *= (M - N + i) / float(i)
            #print ret
        return int(round(ret))
        