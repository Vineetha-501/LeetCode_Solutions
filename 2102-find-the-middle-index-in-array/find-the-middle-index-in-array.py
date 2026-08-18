class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        totalSum = 0
        lftSum = 0

        for i in range(n):
            totalSum += nums[i]
        
        for i in range(n):
            rghtSum = totalSum - lftSum - nums[i]

            if lftSum == rghtSum:
                return i
            else:
                lftSum += nums[i]

        return -1