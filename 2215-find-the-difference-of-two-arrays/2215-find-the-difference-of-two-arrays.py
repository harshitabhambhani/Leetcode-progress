class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)

        result = [
            list(set_nums1 - set_nums2),
            list(set_nums2 - set_nums1)
        ]

        return result

# Example usage:
solution = Solution()
print(solution.findDifference([1,2,3], [2,4,6]))  # Output: [[1,3],[4,6]]
print(solution.findDifference([1,2,3,3], [1,1,2,2]))  # Output: [[3],[]]


        