class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_freq = {}
        
        # Count the frequency of each character
        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1

        # Find the first character with frequency 1
        for i, char in enumerate(s):
            if char_freq[char] == 1:
                return i

        return -1

# Example usage:
solution = Solution()
print(solution.firstUniqChar("leetcode"))
print(solution.firstUniqChar("loveleetcode"))
print(solution.firstUniqChar("aabb"))

        