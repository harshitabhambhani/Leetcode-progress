class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m, n = len(text1), len(text2)
        
        # Create a 2D array to store the lengths of the common subsequences
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill the dp array based on the characters in the strings
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[m][n]

# Test cases
text1_1, text2_1 = "abcde", "ace"
text1_2, text2_2 = "abc", "abc"
text1_3, text2_3 = "abc", "def"

solution = Solution()
print(solution.longestCommonSubsequence(text1_1, text2_1))  # Output: 3
print(solution.longestCommonSubsequence(text1_2, text2_2))  # Output: 3
print(solution.longestCommonSubsequence(text1_3, text2_3))  # Output: 0

        