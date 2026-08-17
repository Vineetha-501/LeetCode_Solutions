class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        n = len(gain)
        altitude = []
        rs = 0
        for i in range(n):
            rs += gain[i]
            altitude.append(rs)

        max = 0
        for i in range(n):
            if altitude[i] > max:
                max = altitude[i]

        if max > 0:
            return max
        else:
            return 0