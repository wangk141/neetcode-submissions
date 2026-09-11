class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        minBuy = prices[0]

        for price in prices:
            maxp = max(maxp, price - minBuy)
            minBuy = min(minBuy, price)
        return maxp