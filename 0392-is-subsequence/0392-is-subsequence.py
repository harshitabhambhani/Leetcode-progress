class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Edge case: an empty string is always a subsequence
        if not s:
            return True

        # Initialize pointers for both strings
        s_ptr, t_ptr = 0, 0

        while t_ptr < len(t):
            if s[s_ptr] == t[t_ptr]:
                s_ptr += 1
                if s_ptr == len(s):
                    return True  # Found all characters of s in order
            t_ptr += 1

        return False

# Example usage:
solution = Solution()
print(solution.isSubsequence("abc", "ahbgdc"))  # Output: True
print(solution.isSubsequence("axc", "ahbgdc"))  # Output: False
