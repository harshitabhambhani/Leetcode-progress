from collections import Counter

class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        counter1 = Counter(word1)
        counter2 = Counter(word2)

        # Check if the sets of characters are the same
        if set(counter1.keys()) != set(counter2.keys()):
            return False

        # Check if the frequency counts are the same
        return sorted(counter1.values()) == sorted(counter2.values())

# Example usage:
solution = Solution()
print(solution.closeStrings("abc", "bca"))  # Output: True
print(solution.closeStrings("a", "aa"))  # Output: False
print(solution.closeStrings("cabbba", "abbccc"))  # Output: True
print(solution.closeStrings("aaabbbbccddeeeeefffff", "aaaaabbcccdddeeeeffff"))  # Output: False


        