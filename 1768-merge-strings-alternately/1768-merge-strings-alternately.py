class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = []
        i, j = 0, 0

        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1

        # Append any remaining letters from word1
        result.extend(word1[i:])

        # Append any remaining letters from word2
        result.extend(word2[j:])

        return ''.join(result)

# Example usage:
sol = Solution()
print(sol.mergeAlternately("abc", "pqr"))   # Output: "apbqcr"
print(sol.mergeAlternately("ab", "pqrs"))   # Output: "apbqrs"
print(sol.mergeAlternately("abcd", "pq"))   # Output: "apbqcd"
