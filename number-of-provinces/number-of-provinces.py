class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = self.buildGraph(isConnected)
        print(graph)
        
        def dfs(node):
            stack = [node]
            while stack:
                node = stack.pop()
                if node in visited:
                    continue
                for neigh in graph[node]:
                    stack.append(neigh)
                    
                visited.add(node)
        
        # Now find the number of connected components
        components = 0
        visited = set()
        for node in graph:
            if node not in visited:
                dfs(node)
                components += 1
            
        return components
        
    def buildGraph(self, isConnected):
        graph = dict()
        for node, connections in enumerate(isConnected):
            graph[node] = set()
            for other_node, connection in enumerate(connections):
                if other_node == node:
                    continue
                if connection == 1:
                    # This means the node is connected to the original node
                    graph[node].add(other_node)
                    
        return graph
            
            