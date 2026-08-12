class Solution(object):
    def minPrice(self, prices, discounts):
        """
        :type prices: List[int]
        :type discounts: List[int]
        :rtype: float
        """
        p = sorted(prices, reverse = True)
        d = sorted(discounts, reverse = True)

        n = min(len(p),len(d))

        s = 0
        for i in range(0,n):
            s += (p[i]*(100-d[i]))/100.0

        s += sum(p[n:])

        return s