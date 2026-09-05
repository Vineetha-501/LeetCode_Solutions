class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            Max = nums[0]
            Min = nums[-1]
            for j in range(0,i+1):
                if nums[j] >= Max:
                    Max = nums[j]
            for a in range(i,n):
                if nums[a] <= Min:
                    Min = nums[a]
            if Max-Min <= k:
                return i

        return -1