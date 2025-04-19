from typing import List


class Solution:
    """
    
    price = [7,6,4,3,1]
    price = [7,1,5,3,6,4]
    price_3 = [2,7,1,5,4]

    🧠 Thought Process (brute-force)
    best_profit = 0
    new need to find best buy and sell price to get best profit
    lets say stock prices = price_3
    if we buy at price price_3[0] == 2
    - then we need to compare the price with rest of the price like
    - sell - buy == profit
        - 7 - 2 = 5
        - 1 - 2 = -1
        - 5 - 2 = 3
        - 4 - 2 = 2
    this is for if we buy at price 2 means we aren't sure if 2 is the best price
    so we need check each price and we don't need to previous price of buy price
    and we need to keep checking till len(price) - 2 as we can buy at last price
    if we can make profit then we can't sell return 0

    🧠 Thought Process (Optimal)
    we can check for on first day for best profit and min price
    lets say [7,1,5,3,6,4] on
    update()
        if min_price > price then min_price = price
        if price - min_price > best_profit best_profit = min_price - price
    
    update
    Day 0: price is 7 and min_price is 7 best_profit is 0
    update
    Day 1: price is 1 and min_price is 1 best profit is 0
    update
    Day 2: price is 5 and min_price is 1 best profit is 4
    update
    Day 3: price is 3 and min_price is 1 best profit is 2
    update
    Day 4: price is 6 and min_price is 1 best profit is 5
    update
    Day 5: price is 4 and min_price is 1 best profit is 3

    Final Explanation:
        We go day by day, keeping track of the lowest price so far (min_price).
        Each day, we check if selling today gives us a better profit (price - min_price) than what we've seen.
        If yes, update max_profit.
        Boom! At the end, we return that

    """
    def bruteForceMaxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                
                best_profit = max(best_profit, profit)
        
        return best_profit
    
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        best_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            
            if price - min_price > best_profit:
                best_profit = price - min_price

        return best_profit





price_3 = [7,6,4,3,1]
sol = Solution().maxProfit(price_3)
print(f"Best profit: {sol}")