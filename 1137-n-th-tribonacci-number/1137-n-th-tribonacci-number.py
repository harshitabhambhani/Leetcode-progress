class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        tribonacci_sequence = [0] * (n + 1)
        tribonacci_sequence[1] = 1
        tribonacci_sequence[2] = 1

        for i in range(3, n + 1):
            tribonacci_sequence[i] = tribonacci_sequence[i - 1] + tribonacci_sequence[i - 2] + tribonacci_sequence[i - 3]

        return tribonacci_sequence[n]

# Example usage:
solution = Solution()
print(solution.tribonacci(4))
print(solution.tribonacci(25))

        