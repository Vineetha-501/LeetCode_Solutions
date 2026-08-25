class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d = {}

        for x in nums:
            d[x] = 1

        i = 1
        while k*i in d:
            i += 1

        return k*i
