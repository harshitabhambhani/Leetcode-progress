class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0

        n = len(matrix)

        for i in range(1, n):
            for j in range(n):
                if j == 0:
                    matrix[i][j] += min(matrix[i - 1][j], matrix[i - 1][j + 1])
                elif j == n - 1:
                    matrix[i][j] += min(matrix[i - 1][j - 1], matrix[i - 1][j])
                else:
                    matrix[i][j] += min(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i - 1][j + 1])

        return min(matrix[-1])

# Example usage:
solution = Solution()
print(solution.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))  # Output: 13
print(solution.minFallingPathSum([[-19,57],[-40,-5]]))  # Output: -59
