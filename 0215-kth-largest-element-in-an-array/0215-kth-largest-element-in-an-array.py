import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_heap = nums[:k]
        heapq.heapify(min_heap)

        for num in nums[k:]:
            if num > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, num)

        return min_heap[0]

# Example usage:
solution = Solution()
print(solution.findKthLargest([3,2,1,5,6,4], 2))  # Output: 5
print(solution.findKthLargest([3,2,3,1,2,4,5,5,6], 4))  # Output: 4

        