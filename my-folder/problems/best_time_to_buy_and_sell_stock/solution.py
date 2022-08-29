class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            if prices[right] > prices[left]:
                current_profit = prices[right] - prices[left]
                max_profit = max(current_profit, max_profit)
                right += 1
            else: 
                left = right
                right += 1
        return max_profit
            
            
        