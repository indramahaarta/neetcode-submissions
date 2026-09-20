from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(set)

        for (x, y) in prerequisites:
            d[x].add(y)
        
        visited = set()
        
        def dfs(x):
            # print(x)
            if x in visited: return False

            if len(d[x]) == 0: return True

            visited.add(x)

            for neigh in d[x]:
                if not dfs(neigh): return False
            
            visited.remove(x)
            
            d[x] = []
            return True


        for i in range(numCourses):
            if not dfs(i): return False

        return True
        
        