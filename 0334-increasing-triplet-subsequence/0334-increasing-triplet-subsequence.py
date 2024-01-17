class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = float('inf')   # Initialize first to positive infinity
        second = float('inf')  # Initialize second to positive infinity

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False

# Example usage:
solution = Solution()
print(solution.increasingTriplet([1,2,3,4,5]))  # Output: True
print(solution.increasingTriplet([5,4,3,2,1]))  # Output: False
print(solution.increasingTriplet([2,1,5,0,4,6]))  # Output: True
