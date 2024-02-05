class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        flips = 0

        while a or b or c:
            bit_a = a & 1
            bit_b = b & 1
            bit_c = c & 1

            if (bit_a | bit_b) != bit_c:
                if bit_c == 1:
                    flips += 1
                else:
                    flips += bit_a + bit_b

            a >>= 1
            b >>= 1
            c >>= 1

        return flips

# Example usage:
solution = Solution()
print(solution.minFlips(2, 6, 5))
print(solution.minFlips(4, 2, 7))
print(solution.minFlips(1, 2, 3))
