# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirror(left,right):
            if not right and not left:
                return True
            if not right or not left:
                return False
            if right.val != left.val:
                return False
            return mirror(left.left,right.right) and mirror(left.right,right.left)
        return mirror(root.left , root.right)