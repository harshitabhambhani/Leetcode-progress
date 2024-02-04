from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""

        # Counter for characters in t
        t_count = Counter(t)
        required_chars = len(t_count)
        
        left, right = 0, 0
        min_len = float('inf')
        result = ""

        # Counter for characters in the current window
        window_count = Counter()

        while right < len(s):
            char = s[right]
            window_count[char] += 1

            if char in t_count and window_count[char] == t_count[char]:
                required_chars -= 1

            while required_chars == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left:right + 1]

                char_left = s[left]
                window_count[char_left] -= 1

                if char_left in t_count and window_count[char_left] < t_count[char_left]:
                    required_chars += 1

                left += 1

            right += 1

        return result

# Example usage:
solution = Solution()
print(solution.minWindow("ADOBECODEBANC", "ABC"))
print(solution.minWindow("a", "a"))
print(solution.minWindow("a", "aa"))
