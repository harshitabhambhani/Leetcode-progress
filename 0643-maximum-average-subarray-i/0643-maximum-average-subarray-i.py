class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # Initialize the sum of the first k elements
        current_sum = sum(nums[:k])
        max_sum = current_sum

        # Iterate through the array and update the sum
        for i in range(k, len(nums)):
            current_sum = current_sum - nums[i - k] + nums[i]
            max_sum = max(max_sum, current_sum)

        # Calculate and return the maximum average
        return float(max_sum) / k

# Example usage:
solution = Solution()
print(solution.findMaxAverage([1,12,-5,-6,50,3], 4))  # Output: 12.75
print(solution.findMaxAverage([5], 1))  # Output: 5.0
