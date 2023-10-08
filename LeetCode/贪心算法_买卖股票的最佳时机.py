class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        minprice = 100000
        maxprofit = 0
        for price in prices :
            minprice = min(minprice,price)
            maxprofit = max(maxprofit,price-minprice)

        return maxprofit