class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 0, 1

        for _ in range(n):
            one, two = two, two + one
        
        return two