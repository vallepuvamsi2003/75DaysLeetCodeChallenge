# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root:
            # Both nodes are in left subtree
            if p.val < root.val and q.val < root.val:
                root = root.left
            
            # Both nodes are in right subtree
            elif p.val > root.val and q.val > root.val:
                root = root.right
            
            # Split happens here → LCA found
            else:
                return root
        