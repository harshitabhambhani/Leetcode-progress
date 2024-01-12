class Solution(object):
    def gcdOfStrings(self, str1, str2):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        len_str1, len_str2 = len(str1), len(str2)
        common_len = gcd(len_str1, len_str2)

        common_str = str1[:common_len]

        # Check if common_str is a valid divisor for both strings
        if str1 == common_str * (len_str1 // common_len) and str2 == common_str * (len_str2 // common_len):
            return common_str
        else:
            return ""

# Example usage:
sol = Solution()
print(sol.gcdOfStrings("ABCABC", "ABC"))    # Output: "ABC"
print(sol.gcdOfStrings("ABABAB", "ABAB"))   # Output: "AB"
print(sol.gcdOfStrings("LEET", "CODE"))     # Output: ""

        