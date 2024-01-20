# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def get_leaf_sequence(root):
            """
            Helper function to get the leaf value sequence for a given tree.
            """
            if not root:
                return []

            if not root.left and not root.right:
                return [root.val]

            left_sequence = get_leaf_sequence(root.left)
            right_sequence = get_leaf_sequence(root.right)

            return left_sequence + right_sequence

        return get_leaf_sequence(root1) == get_leaf_sequence(root2)

        