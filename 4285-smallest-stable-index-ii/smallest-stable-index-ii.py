class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        a = []
        b = []
        Max = nums[0]
        Min = nums[-1]
        n = len(nums)

        for i in range(n):
            if nums[i] >= Max:
                Max = nums[i]
            
            a.append(Max)

        for j in range(n-1,-1,-1):
            if nums[j] <= Min:
                Min = nums[j]

            b.append(Min)

        b = list(reversed(b))

        for i in range(n):
            if a[i]-b[i] <= k:
                return i
                break
        
        return -1