from collections import defaultdict

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = defaultdict(dict)

        # Build the graph
        for (a, b), value in zip(equations, values):
            graph[a][b] = value
            graph[b][a] = 1.0 / value

        def dfs(curr, target, visited):
            if curr == target:
                return 1.0

            visited.add(curr)

            for neighbor, weight in graph[curr].items():
                if neighbor not in visited:
                    product = dfs(neighbor, target, visited)
                    if product != -1.0:
                        return weight * product

            return -1.0

        results = []
        for query in queries:
            source, target = query
            if source not in graph or target not in graph:
                results.append(-1.0)
            else:
                result = dfs(source, target, set())
                results.append(result)

        return results

# Example usage:
solution = Solution()
equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
output = solution.calcEquation(equations, values, queries)
print(output)  # Output: [6.0, 0.5, -1.0, 1.0, -1.0]
