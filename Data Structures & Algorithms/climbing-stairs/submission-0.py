class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            cal = one + two
            two = one
            one = cal
        
        return one