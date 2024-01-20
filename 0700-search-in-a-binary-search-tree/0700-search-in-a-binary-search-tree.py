# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return None
        
        # If the current node's value matches the target value, return the subtree rooted at the current node
        if root.val == val:
            return root
        
        # If the target value is less than the current node's value, search in the left subtree
        if val < root.val:
            return self.searchBST(root.left, val)
        
        # If the target value is greater than the current node's value, search in the right subtree
        return self.searchBST(root.right, val)

# Example usage:
# Construct the binary search tree: [4,2,7,1,3]
root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
# Instantiate the solution class
solution = Solution()
# Search for the subtree with value 2
result = solution.searchBST(root, 2)
# Print the result (subtree)
if result:
    print(result.val, result.left.val, result.right.val)
else:
    print("Subtree not found")
