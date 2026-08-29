class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        Sum = 0
        while n > 0:
            digit = n % 10
            if digit != 0:
                x = x * 10 + digit

            n = n // 10

        rev = 0

        while x > 0:
            digi = x % 10
            rev = rev * 10 + digi
            x = x // 10

        ori_x = rev

        while rev > 0:
            digits = rev % 10
            Sum += digits
            rev = rev // 10

        return ori_x * Sum