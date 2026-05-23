class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l , r = 0 , 1
        profit = 0
        max_profit = 0
        buy = prices[0]
        size = len(prices)
        while r<size:
            if prices[r]<prices[l]:
                l = r
                r+=1
            else:
                profit = prices[r] - prices[l]
                max_profit = max(profit , max_profit)
                r+=1
        return max_profit