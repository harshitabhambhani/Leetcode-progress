class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        # Mapping of digits to letters
        digit_mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(index, current):
            if index == len(digits):
                combinations.append(current)
                return

            digit = digits[index]
            letters = digit_mapping[digit]

            for letter in letters:
                backtrack(index + 1, current + letter)

        combinations = []
        backtrack(0, "")

        return combinations

# Example usage:
solution = Solution()
print(solution.letterCombinations("23"))  # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(solution.letterCombinations(""))    # Output: []
print(solution.letterCombinations("2"))   # Output: ["a","b","c"]

        