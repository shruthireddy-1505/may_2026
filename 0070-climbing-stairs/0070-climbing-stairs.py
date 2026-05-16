class Solution:
    def __init__(self):
        self.d={}
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n in self.d:
            return self.d[n]
        self.d[n] =  self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.d[n]