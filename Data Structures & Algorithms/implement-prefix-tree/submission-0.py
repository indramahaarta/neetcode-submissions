class Node:

    def __init__(self, val: str, is_end: bool):
        self.val = val
        self.is_end = is_end
        self.d = {}
    
    def __str__(self):
        return "{val}, {is_end}, {d}".format(val=self.val, is_end=self.is_end, d=self.d)

class PrefixTree:

    def __init__(self):
        self.root = Node("Root", True)

    def insert(self, word: str) -> None:
        def insert_helper(r: Node, word: str, ptr: int):
            if len(word) == ptr:
                r.is_end = True
                return
            
            ch = word[ptr]
            if ch not in r.d:
                r.d[ch] = Node(ch, False)
            
            insert_helper(r.d[ch], word, ptr+1)
        
        insert_helper(self.root, word, 0)

        # print(self.root)
            

    def search(self, word: str) -> bool:
        ptr = 0
        r = self.root
        while(ptr < len(word)):
            ch = word[ptr]
            if ch not in r.d:
                return False
            
            r = r.d[ch]
            ptr += 1
        
        return r.is_end

    def startsWith(self, prefix: str) -> bool:
        ptr = 0
        r = self.root
        while(ptr < len(prefix)):
            ch = prefix[ptr]
            if ch not in r.d:
                return False
            
            r = r.d[ch]
            ptr += 1
        
        return True
        
        