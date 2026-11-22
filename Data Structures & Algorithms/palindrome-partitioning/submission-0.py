class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []

        def is_palidrome(word):
            # print(word)
            l = 0
            r = len(word) - 1

            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            
            return True
        output = []
        def helper(opt = [], start=0, cur=0):
            if start == len(s):
                return

            if cur == len(s):
                if is_palidrome(s[start:cur]):
                    opt.append(s[start:cur])
                    output.append(list(opt))
                    opt.pop()
                return
            
            # didn't take
            helper(opt, start, cur + 1)

            # take
            if is_palidrome(s[start:cur+1]):
                opt.append(s[start:cur+1])
                helper(opt, cur+1, cur+1)
                opt.pop()
            
            return
        
        helper([], 0, 0)
        return output
        