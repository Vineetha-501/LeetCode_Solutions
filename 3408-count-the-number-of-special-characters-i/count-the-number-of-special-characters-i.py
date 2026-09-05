class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        small = "abcdefghijklmnopqrstuvwxyz"
        capi = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        Small = list(small)
        Capi = list(capi)
        cnt = 0

        n = len(Small)

        for i in range(n):
            if Small[i] in word and Capi[i] in word:
                cnt += 1

        return cnt