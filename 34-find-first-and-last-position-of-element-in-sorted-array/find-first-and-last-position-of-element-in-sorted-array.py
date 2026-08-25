class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        lft = 0
        rght = n-1
        first = -1
        last = -1

        #first
        while lft <= rght:
            mid = lft+(rght-lft)//2

            if nums[mid] == target:
                first = mid
                rght = mid-1
            elif target > nums[mid]:
                lft = mid+1
            else:
                rght = mid-1

        lft = 0
        rght = n-1
        
        #last
        while lft <= rght:
            mid = lft+(rght-lft)//2

            if nums[mid] == target:
                last = mid
                lft = mid+1
            elif target > nums[mid]:
                lft = mid+1
            else:
                rght = mid-1
        
        return [first,last]