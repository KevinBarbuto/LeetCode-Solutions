# Objective: Calculate the sum of the final two numbers of a Fibonacci sequence,
# given the number n of positions to calculate.

class Solution:
    def fib(self, n: int) -> int:
        first = 0 # starting values
        second = 1

        if n == 0:
            return 0
        
        for i in range(n-2):
            fibb = first + second # set next value to sum of previous two
            
            first = second # overwrite starting values
            second = fibb
        
        return first+second
