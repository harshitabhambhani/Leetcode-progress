class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for char in s:
            if char == '*':
                # Remove the closest non-star character and the star itself
                if stack:
                    stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)

# Example usage:
solution = Solution()
print(solution.removeStars("leet**cod*e"))  # Output: "lecoe"
print(solution.removeStars("erase*****"))  # Output: ""

        