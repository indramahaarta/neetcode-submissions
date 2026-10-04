class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        patterns = {}
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + (word[j+1:] if j+1 < len(word) else "")
                
                if pattern not in patterns:
                    patterns[pattern] = []
                
                patterns[pattern].append(word)
        
        adj = {}
        for key, val in patterns.items():
            if len(val) <= 1:
                continue
            
            for i in range(len(val)):
                for j in range(i + 1, len(val)):
                    if val[i] not in adj: adj[val[i]] = []
                    if val[j] not in adj: adj[val[j]] = []

                    adj[val[i]].append(val[j])
                    adj[val[j]].append(val[i])
        # print(adj)
        visited = set()
        def bfs(start, end):
            queue = deque([start])

            ctr = 0
            while queue:
                ctr += 1
                for _ in range(len(queue)):
                    head = queue.popleft()
                    if head in visited:
                        continue
                    visited.add(head)
                
                    if head == end:
                        return ctr

                    if head not in adj: adj[head] = []
                    
                    for nei in adj[head]:
                        queue.append(nei)

            return 0

        return bfs(beginWord, endWord)