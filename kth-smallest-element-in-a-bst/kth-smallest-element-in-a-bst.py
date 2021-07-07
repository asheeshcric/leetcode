# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        sorted_array = self.in_order_traversal(root, [])
        return sorted_array[k - 1]
    
    def in_order_traversal(self, root, result):
        if root is not None:
            if root.left is not None:
                self.in_order_traversal(root.left, result)
            result.append(root.val)
            if root.right is not None:
                self.in_order_traversal(root.right, result)

        return result