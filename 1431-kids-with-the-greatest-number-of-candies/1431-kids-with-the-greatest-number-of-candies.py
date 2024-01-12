class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candies = max(candies)

        result = []
        for kid_candies in candies:
            result.append(kid_candies + extraCandies >= max_candies)

        return result

# Example usage:
sol = Solution()
print(sol.kidsWithCandies([2, 3, 5, 1, 3], 3))
# Output: [True, True, True, False, True]
