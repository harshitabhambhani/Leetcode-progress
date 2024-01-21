from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        queue = deque()
        fresh_count = 0
        minutes = 0

        # Initialize the queue and count the number of fresh oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1

        while queue and fresh_count > 0:
            size = len(queue)
            for _ in range(size):
                i, j = queue.popleft()

                for di, dj in directions:
                    ni, nj = i + di, j + dj

                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        fresh_count -= 1
                        queue.append((ni, nj))

            if queue:
                minutes += 1

        return minutes if fresh_count == 0 else -1

# Example usage:
solution = Solution()
print(solution.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))  # Output: 4
print(solution.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))  # Output: -1
print(solution.orangesRotting([[0,2]]))  # Output: 0
