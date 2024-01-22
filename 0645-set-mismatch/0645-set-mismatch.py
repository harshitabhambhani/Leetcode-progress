class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        expected_sum = (n * (n + 1)) // 2
        actual_sum = sum(nums)

        duplicate = actual_sum - sum(set(nums))
        missing = expected_sum - (actual_sum - duplicate)

        return [duplicate, missing]

# Example usage:
solution = Solution()
print(solution.findErrorNums([1,2,2,4]))  # Output: [2,3]
print(solution.findErrorNums([1,1]))  # Output: [1,2]

        