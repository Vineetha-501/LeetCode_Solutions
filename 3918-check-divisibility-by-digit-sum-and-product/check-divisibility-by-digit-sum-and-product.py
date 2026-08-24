class Solution:
    def checkDivisibility(self, n: int) -> bool:
        ori = n
        Sum = 0
        pro = 1
        while n > 0:
            digit = n % 10
            Sum += digit
            pro *= digit
            n = n // 10

        if ori % (Sum+pro) == 0:
            return True
        
        return False