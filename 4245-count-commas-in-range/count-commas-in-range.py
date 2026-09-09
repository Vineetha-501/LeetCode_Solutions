class Solution:
    def countCommas(self, n: int) -> int:
        ori = n
        cnt = 0
        while n > 0:
            cnt += 1
            n = n//10

        if cnt < 4:
            return 0
        
        return ori - 999