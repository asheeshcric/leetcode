# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        
        def check_balance(node):
            if node is None:
                return -1, True
            
            left_height, left_balanced = check_balance(node.left)
            right_height, right_balanced = check_balance(node.right)
            is_balanced = abs(left_height-right_height)<=1 and left_balanced and right_balanced
            return max(left_height, right_height)+1, is_balanced
        
        return check_balance(root)[1]
        
        