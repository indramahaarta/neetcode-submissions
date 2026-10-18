class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        if len(words) == 1: return words[0]

        def check(w1, w2):
            i = 0
            while i < len(w1) and i < len(w2) and w1[i] == w2[i]:
                if i < len(w1) and w1[i] not in adj:
                    adj[w1[i]] = set()
                i += 1
            if i < len(w1) and i >= len(w2):
                return False
            
            if i < len(w1) and i < len(w2):
                if w1[i] not in adj:
                    adj[w1[i]] = set()
                adj[w1[i]].add(w2[i])
            
            while i < max(len(w1), len(w2)):
                if i < len(w1) and w1[i] not in adj:
                    adj[w1[i]] = set()
                
                if i < len(w2) and w2[i] not in adj:
                    adj[w2[i]] = set()
                
                i+= 1

            return True

        for i in range(1, len(words)):
            if not check(words[i-1], words[i]):
                return ""

        res = ""
        visited = set()

        def dfs(k, process = set()) -> bool:
            nonlocal res
            if k in process:
                return False

            if k in visited:
                return True
            
            visited.add(k)
            process.add(k)
            
            if k not in adj:
                res += k
                return True
            
            for i in adj[k]:
                if not dfs(i, process):
                    return False
            
            res += k
            process.remove(k)
            return True

        for k in adj:
            if not dfs(k):
                return ""
        
        return res[::-1]

        