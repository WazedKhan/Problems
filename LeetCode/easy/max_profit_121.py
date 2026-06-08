from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, cheapest_price = 0, prices[0]
        for price in prices:
            if price < cheapest_price:
                cheapest_price = price
            profit = max(profit, price - cheapest_price)

        return profit
