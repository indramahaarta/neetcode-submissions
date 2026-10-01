class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d = defaultdict(set)

        for (x, y) in prerequisites:
            d[x].add(y)
        
        visited, addedd = set(), set()
        output = []
        
        def dfs(x):
            if x in visited: return False

            if len(d[x]) == 0: 
                if x not in addedd:
                    output.append(x)
                addedd.add(x)
                return True

            visited.add(x)

            for neigh in d[x]:
                if not dfs(neigh): return False
            
            visited.remove(x)
            if x not in addedd:
                output.append(x)
            addedd.add(x)
            
            d[x] = []
            return True


        for i in range(numCourses):
            if not dfs(i): return []

        return output
        

"""
1 > [0, 2, 3]
2 > []
0 > []

"""


        