class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        ---------------------------------------------
        0 1 2 3 4 5 6 7 8 9 10
          ^     ^
            c1:
                s: 3
                t: 3
            
            c4:
                s: 2
                t: 3 

        

        ---------------------------------------------
        0 1 2 3 4 5 6 7 8 9 10
        ^ ^     ^     ^
            c0:
                s:1
                t=10s
            c1:
                s:2
                t=4.5s
            c4:
                s:2
                t=3s
            c7:
                s:1
                t=3s
        
        """

        n_list = []
        for i in range(len(position)):
            n_list.append((position[i], speed[i]))
        
        n_list_sorted = sorted(n_list, key=lambda x:x[0], reverse=True)
        stack = []
        for i in n_list_sorted:
            pos, sp = i
            t = (target - pos)/sp
            
            if stack:
                l_t = stack[-1]
                if l_t >= t:
                    continue

            stack.append(t)

        return len(stack)
        