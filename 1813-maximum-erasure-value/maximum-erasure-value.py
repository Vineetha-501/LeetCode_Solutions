class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        maxs = 0
        res = set()

        for a in range(len(nums)):
            while nums[a] in res:
                res.remove(nums[i])
                i += 1
            res.add(nums[a])
            maxs = max(maxs, sum(res))
            j += 1
        return maxs