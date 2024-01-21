class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        graph = {i: [] for i in range(n)}

        for u, v in connections:
            graph[u].append((v, 1))  # (destination, edge direction: 1 for original, -1 for reversed)
            graph[v].append((u, 0))  # (source, edge direction: 0 for original, 1 for reversed)

        changes = [0]

        def dfs(node, parent):
            for neighbor, direction in graph[node]:
                if neighbor != parent:
                    changes[0] += direction  # Counting the changes needed
                    dfs(neighbor, node)

        dfs(0, -1)  # Start DFS from the capital city (node 0)

        return changes[0]

# Example usage:
solution = Solution()
print(solution.minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]))  # Output: 3
print(solution.minReorder(5, [[1,0],[1,2],[3,2],[3,4]]))  # Output: 2
print(solution.minReorder(3, [[1,0],[2,0]]))  # Output: 0
