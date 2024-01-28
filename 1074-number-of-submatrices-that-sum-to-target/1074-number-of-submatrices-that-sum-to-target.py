class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        rows, cols = len(matrix), len(matrix[0])
        ans = 0

        # Compute the prefix sums for each row
        for row in matrix:
            for i in range(1, cols):
                row[i] += row[i - 1]

        # Fix two columns and find subarray sum in between
        for start_col in range(cols):
            for end_col in range(start_col, cols):
                prefix_sums = {0: 1}
                current_sum = 0

                # Iterate through each row and compute subarray sum
                for row in range(rows):
                    col_sum = matrix[row][end_col] - (matrix[row][start_col - 1] if start_col > 0 else 0)
                    current_sum += col_sum

                    # If current_sum - target exists in prefix_sums, increment count by its frequency
                    if current_sum - target in prefix_sums:
                        ans += prefix_sums[current_sum - target]

                    # Update prefix_sums
                    if current_sum in prefix_sums:
                        prefix_sums[current_sum] += 1
                    else:
                        prefix_sums[current_sum] = 1

        return ans

# Example usage:
solution = Solution()
matrix1 = [[0,1,0],[1,1,1],[0,1,0]]
target1 = 0
print(solution.numSubmatrixSumTarget(matrix1, target1))  # Output: 4

matrix2 = [[1,-1],[-1,1]]
target2 = 0
print(solution.numSubmatrixSumTarget(matrix2, target2))  # Output: 5

matrix3 = [[904]]
target3 = 0
print(solution.numSubmatrixSumTarget(matrix3, target3))  # Output: 0
