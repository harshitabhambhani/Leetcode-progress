class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        i = 0

        while i < len(flowerbed):
            if flowerbed[i] == 0:
                # Check if the current plot and its adjacent plots are empty
                prev_empty = i == 0 or flowerbed[i - 1] == 0
                next_empty = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0

                if prev_empty and next_empty:
                    flowerbed[i] = 1  # Plant a flower
                    count += 1
                    i += 2  # Skip the next plot as it cannot have a flower
                else:
                    i += 1
            else:
                i += 2  # Skip the next plot as it cannot have a flower

        return count >= n

# Example usage:
sol = Solution()
print(sol.canPlaceFlowers([1, 0, 0, 0, 1], 1))  # Output: True
print(sol.canPlaceFlowers([1, 0, 0, 0, 1], 2))  # Output: False        