from collections import deque

class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        m, n = len(maze), len(maze[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        queue = deque([(entrance[0], entrance[1], 0)])
        visited = set([(entrance[0], entrance[1])])

        while queue:
            row, col, steps = queue.popleft()

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                if 0 <= new_row < m and 0 <= new_col < n and maze[new_row][new_col] == '.' and (new_row, new_col) not in visited:
                    if new_row == 0 or new_row == m - 1 or new_col == 0 or new_col == n - 1:
                        return steps + 1  # Reached an exit

                    queue.append((new_row, new_col, steps + 1))
                    visited.add((new_row, new_col))

        return -1  # No exit found

# Example usage:
solution = Solution()
print(solution.nearestExit([["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], [1,2]))  # Output: 1
print(solution.nearestExit([["+","+","+"],[".",".","."],["+","+","+"]], [1,0]))  # Output: 2
print(solution.nearestExit([[".","+"]], [0,0]))  # Output: -1

        