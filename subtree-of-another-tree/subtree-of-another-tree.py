# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def path_string(self, node, string_path):
        if node is None:
            return string_path + '*'
            
        string_path += '_' + str(node.val)
        string_path = self.path_string(node.left, string_path)
        string_path = self.path_string(node.right, string_path)
        return string_path
        
        
        
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        path_s = self.path_string(s, '')
        path_t = self.path_string(t, '')
        print(path_s, path_t)
        return path_t in path_s