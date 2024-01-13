from collections import Counter

class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # Count the occurrences of each character in both strings
        count_s = Counter(s)
        count_t = Counter(t)

        # Calculate the difference in counts
        diff = count_t - count_s

        # Sum the absolute values of the differences to get the minimum steps
        min_steps = sum(abs(diff[char]) for char in diff)

        return min_steps

# Example usage:
solution = Solution()
print(solution.minSteps("bab", "aba"))  # Output: 1
print(solution.minSteps("leetcode", "practice"))  # Output: 5
print(solution.minSteps("anagram", "mangaar"))  # Output: 0 (already anagrams)
