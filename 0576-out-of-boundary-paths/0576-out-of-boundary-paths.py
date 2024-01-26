class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        """
        :type m: int
        :type n: int
        :type maxMove: int
        :type startRow: int
        :type startColumn: int
        :rtype: int
        """
        MOD = 10**9 + 7
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # dp[i][j][k] represents the number of ways to reach cell (i, j) with k moves left
        dp = [[[0] * (maxMove + 1) for _ in range(n)] for _ in range(m)]
        
        # Initialize the base case
        dp[startRow][startColumn][0] = 1
        
        # Update the dp array for each move
        result = 0
        for move in range(1, maxMove + 1):
            temp = [[[0] * (maxMove + 1) for _ in range(n)] for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    for dx, dy in directions:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < m and 0 <= nj < n:
                            temp[i][j][move] = (temp[i][j][move] + dp[ni][nj][move - 1]) % MOD
                        else:
                            result = (result + dp[i][j][move - 1]) % MOD  # Ball moves out of the grid
            dp = temp
        
        return result

# Test cases
solution = Solution()
print(solution.findPaths(2, 2, 2, 0, 0))  # Output: 6
print(solution.findPaths(1, 3, 3, 0, 1))  # Output: 12
