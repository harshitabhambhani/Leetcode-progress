class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        max_vowels = 0
        current_vowels = 0

        # Initialize the count of vowels in the first window
        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1

        max_vowels = current_vowels

        # Iterate through the string with a sliding window
        for i in range(k, len(s)):
            # Update the count of vowels for the current window
            if s[i - k] in vowels:
                current_vowels -= 1
            if s[i] in vowels:
                current_vowels += 1

            # Update the maximum count of vowels
            max_vowels = max(max_vowels, current_vowels)

        return max_vowels

# Example usage:
solution = Solution()
print(solution.maxVowels("abciiidef", 3))  # Output: 3
print(solution.maxVowels("aeiou", 2))  # Output: 2
print(solution.maxVowels("leetcode", 3))  # Output: 2
