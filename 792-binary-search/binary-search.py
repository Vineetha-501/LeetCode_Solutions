class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lft = 0
        rght = n-1

        while lft <= rght:
            mid = lft+(rght-lft)//2

            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                lft = mid+1
            else:
                rght = mid-1

        return -1