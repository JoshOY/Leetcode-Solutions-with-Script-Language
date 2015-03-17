"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
"""


class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        # Special cases
        if len(prices) <= 1:
            return 0
            
        max_profit = 0
        min_buy  = prices[0]
        
        for i in xrange(1, len(prices)):
            min_buy = prices[i - 1] if prices[i - 1] < min_buy else min_buy
            max_profit = (prices[i] - min_buy) if (prices[i] - min_buy > max_profit) else max_profit
        return max_profit