class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0;
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                maxProfit = max(maxProfit, prices[j] - prices[i])
        return maxProfit