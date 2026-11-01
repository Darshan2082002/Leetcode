class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n=len(prices)
        if n<=0:
            return 0 

        dp=[0]*n
        min_prices=prices[0]
        for i in range(1,n):
            min_prices=min(min_prices,prices[i])
            dp[i]=max(dp[i-1],prices[i]-min_prices)
        return dp[-1]            

            
