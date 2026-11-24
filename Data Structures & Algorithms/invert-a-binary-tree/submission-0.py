# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 3 2 1 

        if not root:
            return None

        new_root = root
        stack = [root] # children that needs to be visited
        while stack:
            curr = stack.pop()
            prev_left = curr.left
            prev_right = curr.right

            if prev_left:
                stack.append(prev_left)
            if prev_right:
                stack.append(prev_right)

            curr.left = prev_right
            curr.right = prev_left

        return new_root


            

        