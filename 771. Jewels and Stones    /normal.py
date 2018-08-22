class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        s = 0
        for i in J:
            s += list(S).count(i)
        return s