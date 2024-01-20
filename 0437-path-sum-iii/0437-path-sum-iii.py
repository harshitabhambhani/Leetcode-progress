# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        def count_paths(node, current_sum, target_sum, prefix_sums):
            if not node:
                return 0

            current_sum += node.val
            count = prefix_sums.get(current_sum - target_sum, 0)

            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1

            count += count_paths(node.left, current_sum, target_sum, prefix_sums)
            count += count_paths(node.right, current_sum, target_sum, prefix_sums)

            prefix_sums[current_sum] -= 1

            return count

        prefix_sums = {0: 1}
        return count_paths(root, 0, targetSum, prefix_sums)

        