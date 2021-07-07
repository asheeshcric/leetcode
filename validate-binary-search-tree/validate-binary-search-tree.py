# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.check_validity(root, float("inf"), float("-inf"))
    
    def check_validity(self, root, max_val, min_val):
        if root is None:
            return True
        
        if root.val >= max_val or root.val <= min_val:
            # It means we encountered an invalid node value
            return False
        
        # Traverse to the left such that your max val is the current one
        # Traverse to the right such that your min val is the current one
        return self.check_validity(root.left, root.val, min_val) and self.check_validity(root.right, max_val, root.val)
        