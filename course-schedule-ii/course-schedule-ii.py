from collections import defaultdict
class Solution:
    
    def build_graph(self, projects, dependencies):
        graph = {proj: [] for proj in projects}
        for proj, proj_dep in dependencies:
            graph[proj].append(proj_dep)

        # print(graph.keys())
        return graph
    
    def do_dfs(self, project):
        # print(f'DFS on project {project}')
        # print(f'State: {state}')
        if self.state[project] == 'visiting':
            # A cycle is detected
            return False

        self.state[project] = 'visiting'
        for node in self.graph[project]:
            if self.state[node] == 'visiting':
                # Cycle found
                return False
            if self.state[node] == '':
                if not self.do_dfs(node):
                    return False

        self.state[project] = 'visited'
        self.order.append(project)
        return True
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Initialize variables
        self.state = defaultdict(str)
        self.order = []
        self.graph = self.build_graph(list(range(numCourses)), prerequisites)
        for course in range(numCourses):
            # Do a DFS for each project
            # Check if the project has been already visited state or not
            if self.state[course] == '':
                if not self.do_dfs(course):
                    return []

        return self.order