class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        left, right = 0, len(height) - 1

        while left < right:
            # Calculate the width and height of the container
            width = right - left
            h = min(height[left], height[right])

            # Update the maximum area
            max_area = max(max_area, width * h)

            # Move pointers towards the center
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

# Example usage:
solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))  # Output: 49
print(solution.maxArea([1,1]))  # Output: 1
