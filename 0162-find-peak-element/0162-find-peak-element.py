class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            # Compare mid element with its neighbors
            if nums[mid] > nums[mid + 1]:
                right = mid  # Peak must be in the left half (inclusive)
            else:
                left = mid + 1  # Peak must be in the right half

        return left  # Left or right can be returned, as they converge to the peak index

# Example usage:
solution = Solution()
print(solution.findPeakElement([1, 2, 3, 1]))  # Output: 2
print(solution.findPeakElement([1, 2, 1, 3, 5, 6, 4]))  # Output: 5

        