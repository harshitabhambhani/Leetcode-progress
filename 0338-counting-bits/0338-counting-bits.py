class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # Initialize an array to store the count of 1's for each number from 0 to n
        result = [0] * (n + 1)

        for i in range(1, n + 1):
            # Use the recurrence relation to calculate the count of 1's
            result[i] = result[i // 2] + i % 2

        return result

# Example usage:
solution = Solution()
print(solution.countBits(2))
print(solution.countBits(5))

        