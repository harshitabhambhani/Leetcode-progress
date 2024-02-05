class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        
        # Sort intervals based on end points
        intervals.sort(key=lambda x: x[1])
        
        # Initialize variables
        count = 1  # Number of non-overlapping intervals
        end = intervals[0][1]  # End point of the first interval
        
        # Iterate through sorted intervals
        for i in range(1, len(intervals)):
            start, current_end = intervals[i]
            
            # If the current interval doesn't overlap with the previous selected interval
            if start >= end:
                count += 1
                end = current_end
        
        # Calculate the number of intervals to be removed
        removals = len(intervals) - count
        return removals
sol = Solution()
intervals1 = [[1,2],[2,3],[3,4],[1,3]]
print(sol.eraseOverlapIntervals(intervals1))  # Output: 1

intervals2 = [[1,2],[1,2],[1,2]]
print(sol.eraseOverlapIntervals(intervals2))  # Output: 2

intervals3 = [[1,2],[2,3]]
print(sol.eraseOverlapIntervals(intervals3))  # Output: 0

        