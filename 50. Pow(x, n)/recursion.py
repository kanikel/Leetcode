Solution 1:

        # recursion 关键是理解递归的本质就是数学归纳法，除非算法错不然肯定会成功
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1/x
        return self.myPow(x*x, n/2) if n % 2 == 0 else x * self.myPow(x*x, (n-1)/2)

Soluiton 2:

        # recursion
        if n == 0:
            return 1
        if n < 0:
            return x/self.myPow(x, -(n-1))  #这里是为了防止n取-2^31的情况，不过Python好像C++/Java不同，对这个限制不明显
        elif n % 2:
            return x*self.myPow(x*x, (n-1)/2)
        else:
            return self.myPow(x*x, n/2)