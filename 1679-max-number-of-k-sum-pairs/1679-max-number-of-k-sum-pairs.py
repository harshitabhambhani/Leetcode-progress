from collections import defaultdict

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq_map = defaultdict(int)
        operations_count = 0

        for num in nums:
            complement = k - num

            if freq_map[complement] > 0:
                # Found a pair, decrement frequencies and increment operations count
                freq_map[complement] -= 1
                operations_count += 1
            else:
                # Update frequency of the current element
                freq_map[num] += 1

        return operations_count

# Example usage:
solution = Solution()
print(solution.maxOperations([1,2,3,4], 5))  # Output: 2
print(solution.maxOperations([3,1,3,4,3], 6))  # Output: 1

        