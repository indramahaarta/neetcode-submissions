class Node:
    
    def __init__(self, isEnd):
        self.isEnd = isEnd
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = Node(True)

    def addWord(self, word: str) -> None:
        cur = self.root

        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Node(False)
            
            cur = cur.children[ch]
        
        cur.isEnd = True

    def search(self, word: str) -> bool:
        def search_helper(cur, word, i):
            if len(word) == i:
                return cur.isEnd
            
            if word[i] != "." and word[i] not in cur.children:
                return False
            
            if word[i] == '.':
                for ch in cur.children:
                    if search_helper(cur.children[ch], word, i+1):
                        return True
                
                return False

            return search_helper(cur.children[word[i]], word, i +1)
            
            
        
        return search_helper(self.root, word, 0)
