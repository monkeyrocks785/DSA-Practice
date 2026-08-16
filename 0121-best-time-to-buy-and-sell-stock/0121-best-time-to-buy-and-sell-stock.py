class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mxp = 0
        mnp = float('inf')
        for i in range(len(prices)):
            mnp = min(mnp, prices[i])
            mxp = max(mxp, prices[i] - mnp)

        return mxp