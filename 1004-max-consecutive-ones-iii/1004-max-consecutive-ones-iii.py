class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left, right = 0, 0
        max_length = 0
        zero_count = 0

        while right < len(nums):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_length = max(max_length, right - left + 1)
            right += 1

        return max_length

# Example usage:
solution = Solution()
print(solution.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))  # Output: 6
print(solution.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))  # Output: 10

        