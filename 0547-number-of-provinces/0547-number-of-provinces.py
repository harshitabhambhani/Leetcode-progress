class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        provinces = 0
        visited = set()

        def dfs(city):
            visited.add(city)
            for neighbor, connected in enumerate(isConnected[city]):
                if connected == 1 and neighbor not in visited:
                    dfs(neighbor)

        for city in range(n):
            if city not in visited:
                provinces += 1
                dfs(city)

        return provinces

# Example usage:
solution = Solution()
print(solution.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))  # Output: 2
print(solution.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))  # Output: 3
