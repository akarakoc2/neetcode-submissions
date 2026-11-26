# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        counter = 1
        if root.left and root.right:
            counter += max(self.maxDepth(root.left), self.maxDepth(root.right))
            
            
        elif root.left and not root.right:
            counter += self.maxDepth(root.left)
            
        elif root.right and not root.left:
            counter += self.maxDepth(root.right)
            
        return counter
