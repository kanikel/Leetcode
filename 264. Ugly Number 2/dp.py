class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 题意等于要找到序号为n的丑数，要把所有的丑数都给列举出来？
        # 思考：有什么重复的步骤？找丑数不如找非丑数，你的方法效率太低了，按照顺序从1到无限大一个个再去判断是否为丑数很明显会MLE和TLE
        # 总结：思考的方向错了，为什么错了，因为对time和space还是没有很清晰的概念！
        # time: O(n * 3) = O(n)
        # spce: O(n) store the n ugly number
        ugly = [1] * n
        i2, i3, i5 = 0, 0, 0
        for i in range(1, n):
            ugly[i] = min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5)
            if ugly[i] == ugly[i2]*2: i2 += 1
            if ugly[i] == ugly[i3]*3: i3 += 1
            if ugly[i] == ugly[i5]*5: i5 += 1
        return ugly[n-1]