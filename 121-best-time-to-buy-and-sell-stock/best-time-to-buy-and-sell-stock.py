class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0

        for i in range(1, len(prices)):
            minPrice = min(prices[i], minPrice)
            maxProfit = max(maxProfit, prices[i] - minPrice)
        
        return maxProfit