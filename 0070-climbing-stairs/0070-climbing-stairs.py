class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2

        # Initialize the first two Fibonacci numbers
        first, second = 1, 2

        for _ in range(3, n + 1):
            # Calculate the next Fibonacci number
            current = first + second
            # Update first and second for the next iteration
            first, second = second, current

        return second

# Example usage:
solution = Solution()
print(solution.climbStairs(2))  # Output: 2
print(solution.climbStairs(3))  # Output: 3
