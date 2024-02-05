class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        
        # Sort balloons based on end points
        points.sort(key=lambda x: x[1])
        
        arrows = 1  # Initialize the number of arrows to 1
        end = points[0][1]  # End point of the first balloon
        
        # Iterate through sorted balloons
        for i in range(1, len(points)):
            start, current_end = points[i]
            
            # If the start point is greater than the current arrow position
            if start > end:
                arrows += 1
                end = current_end
        
        return arrows

sol = Solution()
points1 = [[10,16],[2,8],[1,6],[7,12]]
print(sol.findMinArrowShots(points1))  # Output: 2

points2 = [[1,2],[3,4],[5,6],[7,8]]
print(sol.findMinArrowShots(points2))  # Output: 4

points3 = [[1,2],[2,3],[3,4],[4,5]]
print(sol.findMinArrowShots(points3))  # Output: 2

        