class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Brute Force
        - Initialize profit at 0
        - Create nested for loop
        - For every variation, calculate profit
        - Record maximum profit
        - Return maximum profit
        Time: n^2
        Space: 1

        Optimized
        - Initialize l at 0
        - Initialize r at 1
        - Initialize profit at 0
        - while r < len(prices)
            calculate curr_profit
            if curr_profit > profit, profit = curr_profit
            if curr_profit < 0, l = r
            r += 1
        - return profit
        """
        l, r = 0, 1
        profit = 0

        while r < len(prices):
            curr_profit = prices[r] - prices[l]
            profit = max(profit, curr_profit)
            if curr_profit < 0:
                l = r
            r += 1
        
        return profit