class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1

        prefix = [0]*len(nums)
        prefix[0] = nums[0]

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1]+nums[i]

        total = prefix[-1]

        for i in range(len(nums)):
            if i == 0:
                lft = 0
            else:
                lft = prefix[i-1]

            rght = total-prefix[i]

            if lft == rght:
                return i

        return -1