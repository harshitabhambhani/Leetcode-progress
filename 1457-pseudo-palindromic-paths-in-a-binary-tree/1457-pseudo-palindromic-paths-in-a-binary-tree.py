class Solution(object):
    def pseudoPalindromicPaths(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def is_pseudo_palindrome(counts):
            odd_count = 0
            for count in counts:
                if count % 2 == 1:
                    odd_count += 1
                    if odd_count > 1:
                        return False
            return True
        
        def dfs(node, counts):
            if not node:
                return 0
            
            counts[node.val - 1] += 1
            
            if not node.left and not node.right:
                result = 1 if is_pseudo_palindrome(counts) else 0
            else:
                result = dfs(node.left, counts[:]) + dfs(node.right, counts[:])
            
            counts[node.val - 1] -= 1
            
            return result
        
        return dfs(root, [0] * 9)
