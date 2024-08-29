# Objective: Return number of possible ways to climb stairs,
# assuming you can ascend either one or two steps at a time.

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: # Handles simplest cases
            return n
        
        # Applies Fibonacci algorithm
        first = 1
        second = 2
        fib = 0
        for i in range(2,n):
            fib = first + second
            first = second
            second = fib
        
        return fib
