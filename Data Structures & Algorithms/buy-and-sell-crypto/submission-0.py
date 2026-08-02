class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curMin, prevMax = 0, 0

        for i, val in enumerate(prices):
            if val < prices[curMin]:
                curMin = i
            else:
                prevMax = max(prevMax, val - prices[curMin])
        
        return prevMax
        