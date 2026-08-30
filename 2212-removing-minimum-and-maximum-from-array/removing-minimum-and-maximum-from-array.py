class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        a = max(nums)
        b = min(nums)
        n = len(nums)
        c = []
        d = []

        for i in range(n):
            if nums[i] == a or nums[i] == b:
                c.append(i+1)

        for i in range(n-1, -1, -1):
            if nums[i] == a or nums[i] == b:
                d.append(n-i)

        e = max(c)
        f = max(d)
        g = min(c)+min(d)

        return min(e,f,g)