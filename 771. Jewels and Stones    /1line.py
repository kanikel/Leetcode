class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """

        #s = sum(i in J for i in S)
        return sum([i in J for i in S])