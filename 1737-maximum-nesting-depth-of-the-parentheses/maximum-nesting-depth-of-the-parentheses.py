class Solution:
    def maxDepth(self, s: str) -> int:
        dep = 0
        max_dep = 0

        for ch in s:
            if ch == '(':
                dep += 1
                max_dep = max(max_dep, dep)
            elif ch == ')':
                dep -= 1

        return max_dep