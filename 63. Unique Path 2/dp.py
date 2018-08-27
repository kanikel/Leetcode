class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # time:O(mn)
        # space: O(mn)
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[None] * n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                for k in range(i, m):
                    dp[k][0] = 0
                break
            else:
                dp[i][0] = 1
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                for k in range(j, n):
                    dp[0][k] = 0
                break
            else:
                dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else: dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]