# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flattenTree(self, node):
        # For each node, we need:
        # a. First, flatten the left side
        # b. Second, flatten the right side
        # c. Return the tails of left and right flattened sides
        if node is None:
            return None
        
        # If the current node is a leaf node, we just return the node
        if node.left is None and node.right is None:
            return node
        
        # Recursively flatten the left subtree
        left_tail = self.flattenTree(node.left)
        
        # Recursively flatten the right subtree
        right_tail = self.flattenTree(node.right)
        
        # If we encounter a leftTail, we shuffle the connections around
        if left_tail:
            left_tail.right = node.right
            node.right = node.left
            node.left = None
            
        return right_tail if right_tail else left_tail
    
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.flattenTree(root)
        