class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        temp = []
        def bfs(i, cur_arr, cur_total):
            if cur_total == target:
                res.append(cur_arr.copy())
                return
                
            if i >= len(candidates) or cur_total > target:
                return
            
            # choose 
            cur_arr.append(candidates[i])
            bfs(i+1, cur_arr, cur_total + candidates[i])
            cur_arr.pop()

            # don't choose, go to the next index
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            bfs(i+1, cur_arr, cur_total)
        
        bfs(0, [], 0)
        return res



        