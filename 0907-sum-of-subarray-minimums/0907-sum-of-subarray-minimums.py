class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        stack = []
        result = 0
        arr.append(0)  # Ensure all elements in the stack are popped at the end

        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] >= num:
                idx = stack.pop()
                result += arr[idx] * (i - idx) * (idx - (stack[-1] if stack else -1))

            stack.append(i)

        return result % MOD

# Example usage:
solution = Solution()
print(solution.sumSubarrayMins([3, 1, 2, 4]))  # Output: 17
print(solution.sumSubarrayMins([11, 81, 94, 43, 3]))  # Output: 444

        