# Objective: Given a list (representing a series of stock prices after certain time intervals), 
# determine the greatest profit that can be made, assuming that the "buy low, sell high" 
# investment strategy is employed.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Set initial pointer values
        L = 0
        R = 1
        maxProfit = 0
        
        # Loop through the list using the pointers
        while R < len(prices):
            if prices[L] < prices[R]:
                profit = prices[R] - prices[L]
                maxProfit = max(maxProfit, profit)
            else:
                L = R
            R += 1
        
        return maxProfit
