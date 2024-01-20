# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None

        # Recursive search for the node to be deleted
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node with only one child or no child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            root.val = self.findMin(root.right).val
            # Delete the inorder successor
            root.right = self.deleteNode(root.right, root.val)

        return root

    def findMin(self, node):
        # Find the leftmost leaf in the subtree
        while node.left:
            node = node.left
        return node

# Example usage:
# Construct the binary search tree: [5,3,6,2,4,null,7]
root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))
# Instantiate the solution class
solution = Solution()
# Delete the node with value 3
result = solution.deleteNode(root, 3)
# Print the result (in-order traversal of the modified tree)
def inOrderTraversal(node):
    if node:
        inOrderTraversal(node.left)
        print(node.val),
        inOrderTraversal(node.right)

inOrderTraversal(result)

