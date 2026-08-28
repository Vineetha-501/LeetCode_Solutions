class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        ans = 0
        freq = {}

        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        for i,cnt in freq.items():
            if cnt == 1:
                ans = i

        return ans