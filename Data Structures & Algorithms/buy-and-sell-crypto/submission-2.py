class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        best_profit = 0

        for price in prices:
            profit = price - lowest
            if profit > best_profit:
                best_profit = profit

            if price < lowest:
                lowest = price

        return best_profit