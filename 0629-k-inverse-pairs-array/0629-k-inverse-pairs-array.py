class Solution(object):
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7

        # Initialize the dp array
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        # Base case: there is one permutation of 0 elements with 0 inverse pairs
        dp[0][0] = 1

        for i in range(1, n + 1):
            dp[i][0] = 1  # No inverse pairs for an empty permutation
            for j in range(1, k + 1):
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % MOD
                if j >= i:
                    dp[i][j] = (dp[i][j] - dp[i - 1][j - i] + MOD) % MOD

        return dp[n][k]

# Test cases
solution = Solution()
print(solution.kInversePairs(3, 0))  # Output: 1
print(solution.kInversePairs(3, 1))  # Output: 2

        