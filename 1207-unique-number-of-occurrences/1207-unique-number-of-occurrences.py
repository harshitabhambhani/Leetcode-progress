from collections import Counter

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # Count the occurrences of each value in the array
        count_dict = Counter(arr)

        # Check if the count of occurrences is unique
        unique_counts = set(count_dict.values())
        return len(unique_counts) == len(count_dict)

# Example usage:
solution = Solution()
print(solution.uniqueOccurrences([1,2,2,1,1,3]))  # Output: True
print(solution.uniqueOccurrences([1,2]))  # Output: False
print(solution.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))  # Output: True
