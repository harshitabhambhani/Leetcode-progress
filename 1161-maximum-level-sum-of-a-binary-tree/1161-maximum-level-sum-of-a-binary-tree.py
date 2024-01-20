from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        max_sum = float('-inf')
        max_level = 0

        queue = deque([root])
        level = 1

        while queue:
            level_sum = sum(node.val for node in queue)
            
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level

            level += 1
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return max_level

# Example usage:
# Construct the binary tree: [1,7,0,7,-8,null,null]
root = TreeNode(1, TreeNode(7, TreeNode(7), TreeNode(-8)), TreeNode(0))
# Instantiate the solution class
solution = Solution()
# Find and print the level with the maximal sum
print(solution.maxLevelSum(root))

        