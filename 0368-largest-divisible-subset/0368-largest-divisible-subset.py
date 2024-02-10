class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Sort the input list
        nums.sort()
        
        # Initialize a list to store the length of the largest divisible subset ending at each index
        dp = [1] * len(nums)
        
        # Initialize variables to store the length of the largest subset and its ending index
        max_len = 1
        max_index = 0
        
        # Iterate through the list
        for i in range(len(nums)):
            # Iterate through all previous elements
            for j in range(i):
                # If nums[i] is divisible by nums[j], update dp[i]
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
            
            # Update the maximum length and ending index
            if dp[i] > max_len:
                max_len = dp[i]
                max_index = i
        
        # Reconstruct the largest divisible subset using the dp array and the maximum ending index
        subset = []
        current_len = max_len
        current_index = max_index
        for i in range(max_index, -1, -1):
            if dp[i] == current_len and nums[current_index] % nums[i] == 0:
                subset.append(nums[i])
                current_len -= 1
                current_index = i
        
        return subset[::-1]

        