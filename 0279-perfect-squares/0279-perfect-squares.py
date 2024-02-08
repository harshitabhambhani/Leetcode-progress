class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Initialize a list to store the minimum number of perfect squares for each integer up to n
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        # Iterate through all integers from 1 to n
        for i in range(1, n + 1):
            # Iterate through all possible perfect squares less than or equal to i
            j = 1
            while j * j <= i:
                # Update the minimum number of perfect squares for i
                dp[i] = min(dp[i], dp[i - j*j] + 1)
                j += 1
        
        return dp[n]

        