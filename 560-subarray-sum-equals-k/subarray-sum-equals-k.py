class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0:1}
        subCnt = 0
        prefixSum = 0
        for i in nums:
            # Compute the prefix sum
            prefixSum += i
            # Calculate the required previous prefix we have to search
            req = prefixSum - k
            # Check if req in seen prefixes (history of prefixes)
            if req in seen:
                # Add the value to subCnt
                subCnt += seen[req]

            # Crucial step: Add the current prefixSum to history (seen)
            seen[prefixSum] = seen.get(prefixSum,0)+1
        return subCnt