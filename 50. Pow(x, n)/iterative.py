class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # 这是迭代的方法，记住是最后才令r *= x，先是不停地组合x
        if n == 0:
            return 1
        m = abs(n)
        r = float(1)        
        while m > 0:
            if m % 2 != 0:
                r = x * r
                m -= 1
            else:
                x = x * x
                m = m / 2
                #print x, m
                
        return r if n > 0 else 1/r