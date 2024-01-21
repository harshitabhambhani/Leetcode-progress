class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        n = len(nums)
        if n == 1:
            return nums[0]

        # Create an array to store the maximum amount of money robbed up to each house
        dp = [0] * n

        # Initialize the first two elements
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # Iterate over the rest of the houses
        for i in range(2, n):
            # Choose the maximum amount between robbing the current house or skipping it
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        # The last element in dp contains the maximum amount of money that can be robbed
        return dp[-1]

# Example usage:
solution = Solution()
print(solution.rob([1, 2, 3, 1]))  # Output: 4
print(solution.rob([2, 7, 9, 3, 1]))  # Output: 12

        