class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq = {}
        maxlen = 0
        i = 0

        for j in range(len(nums)):
            if nums[j] in freq:
                freq[nums[j]] += 1
            else:
                freq[nums[j]] = 1
            
            while freq[nums[j]] > k:
                freq[nums[i]] -= 1
                i += 1

            maxlen = max(maxlen, j-i+1)

        return maxlen