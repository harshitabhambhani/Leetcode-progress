class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if not chars:
            return 0

        write_idx = 0  # Index for writing compressed characters
        curr_char = chars[0]  # Current character being processed
        count = 1  # Count of consecutive occurrences

        for i in range(1, len(chars)):
            if chars[i] == curr_char:
                count += 1
            else:
                chars[write_idx] = curr_char
                write_idx += 1

                if count > 1:
                    count_str = str(count)
                    for digit in count_str:
                        chars[write_idx] = digit
                        write_idx += 1

                curr_char = chars[i]
                count = 1

        # Write the last character and its count (if greater than 1)
        chars[write_idx] = curr_char
        write_idx += 1

        if count > 1:
            count_str = str(count)
            for digit in count_str:
                chars[write_idx] = digit
                write_idx += 1

        return write_idx

# Example usage:
solution = Solution()
chars1 = ["a", "a", "b", "b", "c", "c", "c"]
print(solution.compress(chars1))  # Output: 6, chars1[:6] = ["a", "2", "b", "2", "c", "3"]

chars2 = ["a"]
print(solution.compress(chars2))  # Output: 1, chars2[:1] = ["a"]

chars3 = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
print(solution.compress(chars3))  # Output: 4, chars3[:4] = ["a", "b", "1", "2"]
