class TrieNode:
    def __init__(self, isEnd = False):
        self.children = {}
        self.isEnd = isEnd
        self.isRes = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode(True)
    
    def insert(self, word):
        root = self.root

        for ch in word:
            if ch not in root.children:
                root.children[ch] = TrieNode()
            
            root = root.children[ch]
        
        root.isEnd = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        t = Trie()

        for word in words:
            t.insert(word)
        
        def dfs(row: int, col: int, n: TrieNode, s: set):
            ch = board[row][col]
            if ch not in n.children:
                return

            node = n.children[ch]
            if node.isEnd:
                node.isRes = True
            
            directions = [(row,col+1), (row,col-1), (row+1,col), (row-1,col)]
            s.add((row, col))
            for nextRow, nextCol in directions:
                if (nextRow, nextCol) in s:
                    continue
                
                if nextRow < 0 or nextCol < 0 or nextRow >= len(board) or nextCol >= len(board[0]):
                    continue

                
                dfs(nextRow, nextCol, node, s)
            s.remove((row, col))

        for row in range(len(board)):
            for col in range(len(board[row])):
                dfs(row, col, t.root, set((row, col)))
            
        res = set()
        def dfs2(t: TrieNode, curWord = ""):
            for k, v in t.children.items():
                print(k, v.isRes, v.isEnd)
                word = curWord + k
                if v.isRes:
                    res.add(word)
                
                dfs2(v, word)
        
        dfs2(t.root, "")
        
        return list(res)



        

        
        