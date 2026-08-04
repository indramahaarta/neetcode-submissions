class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        m = {}
        for task in tasks:
            m[task] = m.get(task, 0) + 1
        
        l = []
        for val in m.values():
            l.append(-val)
        heapq.heapify(l)

        time = 0
        queue = deque()
        
        while l or queue:
            # print(time, l, queue)
            if l:
                val = heapq.heappop(l)
                val = 1 + val

                if val:
                    queue.append((val, time + n))
            
            if queue and queue[0][1] == time:
                heapq.heappush(l, queue.popleft()[0])
            
            time += 1
        
        return time

        
        
        