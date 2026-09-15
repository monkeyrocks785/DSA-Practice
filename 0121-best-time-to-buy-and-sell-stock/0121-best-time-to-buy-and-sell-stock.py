class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mxp = 0
        mnp = float('inf')

        for i in prices:
            mnp = min(mnp, i)
            pro = i - mnp
            mxp = max(mxp, pro)
        
        return mxp