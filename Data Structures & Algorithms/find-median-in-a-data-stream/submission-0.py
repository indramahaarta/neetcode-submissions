class MedianFinder:

    def __init__(self):
        self.mxHeap = []
        self.mnHeap = []

    def addNum(self, num: int) -> None:
        h = self.mnHeap[0] if self.mnHeap else 0
        if num < h:
            heapq.heappush(self.mxHeap, num * -1)
        else:
            heapq.heappush(self.mnHeap, num)
        
        if abs(len(self.mxHeap) - len(self.mnHeap)) > 1:
            if len(self.mxHeap) > len(self.mnHeap):
                head = heapq.heappop(self.mxHeap) * - 1
                heapq.heappush(self.mnHeap, head)
            else:
                head = heapq.heappop(self.mnHeap)
                heapq.heappush(self.mxHeap, head * -1)

    def findMedian(self) -> float:
        # print(self.mxHeap, self.mnHeap)
        if len(self.mxHeap) > len(self.mnHeap): return self.mxHeap[0] * -1
        elif len(self.mnHeap) > len(self.mxHeap): return self.mnHeap[0]
        else:
            headMn = self.mnHeap[0]
            headMx = self.mxHeap[0] * -1
            return (headMn + headMx) / 2
        
        