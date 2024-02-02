class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        result = []
        
        for length in range(len(str(low)), len(str(high)) + 1):
            for start in range(1, 10 - length + 1):
                num = int(''.join(str(start + i) for i in range(length)))
                if low <= num <= high:
                    result.append(num)
        
        return result

# Example usage:
solution = Solution()
print(solution.sequentialDigits(100, 300))
print(solution.sequentialDigits(1000, 13000))

        