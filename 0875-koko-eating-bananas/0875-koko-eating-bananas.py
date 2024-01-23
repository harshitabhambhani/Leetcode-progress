class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def can_finish(speed):
            # Calculate hours needed to finish eating with the given speed
            hours = sum((pile + speed - 1) // speed for pile in piles)
            return hours <= h

        # Binary search to find the minimum eating speed
        left, right = 1, max(piles)

        while left < right:
            mid = left + (right - left) // 2

            if can_finish(mid):
                right = mid  # Minimum speed is in the left half (inclusive)
            else:
                left = mid + 1  # Minimum speed is in the right half

        return left

# Example usage:
solution = Solution()
print(solution.minEatingSpeed([3, 6, 7, 11], 8))  # Output: 4
print(solution.minEatingSpeed([30, 11, 23, 4, 20], 5))  # Output: 30
print(solution.minEatingSpeed([30, 11, 23, 4, 20], 6))  # Output: 23

        