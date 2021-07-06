"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        
        new_node_neighbors = dict()
        return self.dfs(node, new_node_neighbors)
    
    def dfs(self, node, new_node_neighbors):
        if node.val in new_node_neighbors:
            # We already created a node for that value
            return new_node_neighbors[node.val]
        
        new_copy = Node(val=node.val)
        new_node_neighbors[node.val] = new_copy
        for neighbor in node.neighbors:
            new_copy.neighbors.append(self.dfs(neighbor, new_node_neighbors))
            
        return new_copy