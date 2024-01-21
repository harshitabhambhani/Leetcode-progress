class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        n = len(rooms)
        visited = set()

        def dfs(room):
            if room in visited:
                return
            visited.add(room)
            for key in rooms[room]:
                dfs(key)

        dfs(0)
        return len(visited) == n

# Example usage:
solution = Solution()
print(solution.canVisitAllRooms([[1], [2], [3], []]))  # Output: True
print(solution.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))  # Output: False
