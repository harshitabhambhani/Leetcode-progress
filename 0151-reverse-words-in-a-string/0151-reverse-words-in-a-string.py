class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()  # Split the string into a list of words
        reversed_words = reversed(words)  # Reverse the list of words
        result = ' '.join(reversed_words)  # Join the reversed words with a single space

        return result

# Example usage:
solution = Solution()
print(solution.reverseWords("the sky is blue"))  # Output: "blue is sky the"
print(solution.reverseWords("  hello world  "))  # Output: "world hello"
print(solution.reverseWords("a good   example"))  # Output: "example good a"
