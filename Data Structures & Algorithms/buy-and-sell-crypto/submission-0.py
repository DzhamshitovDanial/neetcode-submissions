class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx=0
        minp=prices[0]
        for i in range(1,len(prices)):
            if prices[i]<minp:
                minp=prices[i]
            elif prices[i]-minp>mx:
                mx=prices[i]-minp
        return mx