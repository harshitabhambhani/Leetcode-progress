class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set("aeiouAEIOU")
        s_list = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and s_list[left].lower() not in vowels:
                left += 1
            while left < right and s_list[right].lower() not in vowels:
                right -= 1

            # Swap vowels
            s_list[left], s_list[right] = s_list[right], s_list[left]

            left += 1
            right -= 1

        return ''.join(s_list)

# Example usage:
solution = Solution()
print(solution.reverseVowels("hello"))  # Output: "holle"
print(solution.reverseVowels("leetcode"))  # Output: "leotcede"
