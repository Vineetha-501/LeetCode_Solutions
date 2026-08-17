class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        prefixSum = []
        rs = 0
        for i in range(n):
            rs += nums[i]
            prefixSum.append(rs)

        return prefixSum