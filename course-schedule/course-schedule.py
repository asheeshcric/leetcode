class Solution:
    def canFinish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        graph = self.create_graph(num_courses, prerequisites)
        visit_set = set()
        
        def dfs(course):
            if course in visit_set:
                # We are already visiting this course and found a cycle
                return False
            
            if not graph[course]:
                # Since it does not have any prereq, we can take this course
                return True
            
            visit_set.add(course)
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
                
        
            # Finally, we know that we can take this course. So, we need to remove it from the visit set
            visit_set.remove(course)
            graph[course] = [] # Making prereq empty as we already know that this can be taken
            return True
        
        # Now, checking the same thing for all courses manually as the graph may not be fully connected
        for course in range(num_courses):
            if not dfs(course):
                return False
            
        return True
    
    
    def create_graph(self, num_courses, prerequisites):
        graph = {i: [] for i in range(num_courses)}
        for course, prereq in prerequisites:
            graph[course].append(prereq)
            
        return graph