class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, 0
        max_length = 0
        zero_count = 0

        while right < len(nums):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_length = max(max_length, right - left + 1)
            right += 1

        # If max_length is equal to the length of the array, return max_length - 1
        # This is because we can only delete one element, so the longest subarray is one less than the array length
        return max_length - 1 if max_length > 0 else 0

# Example usage:
solution = Solution()
print(solution.longestSubarray([1,1,0,1]))  # Output: 3
print(solution.longestSubarray([0,1,1,1,0,1,1,0,1]))  # Output: 5
print(solution.longestSubarray([1,1,1]))  # Output: 2        