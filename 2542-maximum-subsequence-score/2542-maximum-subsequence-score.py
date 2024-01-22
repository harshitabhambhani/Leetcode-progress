from heapq import heappush, heappop

class Solution:
    def maxScore(self, nums1, nums2, k):
        nums = sorted(zip(nums2, nums1), reverse=True)
        q = []
        ans = s = 0
        for a, b in nums:
            s += b
            heappush(q, b)
            if len(q) == k:
                ans = max(ans, s * a)
                s -= heappop(q)
        return ans

# Example usage:
solution = Solution()
print(solution.maxScore([1, 3, 3, 2], [2, 1, 3, 4], 3))  # Output: 12
print(solution.maxScore([4, 2, 3, 1, 1], [7, 5, 10, 9, 6], 1))  # Output: 30
