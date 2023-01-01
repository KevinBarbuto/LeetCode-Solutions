# Objective: Take a string and given string and modify it to become reversed.
# Constraint: For some reason, LeetCode will accept the trivial solution of simply writing "s.reverse()" and calling it a day. 
# I felt this was too boring, so I made it more challenging on myself and attempted more of a stack-based solution.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        j = 0
        stack = [] # Initialize a stack to push / pull from.
        for i in s:
            stack.append(i)
        
        # Iterate through the newly created stack
        while stack:
            s[j] = stack.pop() # Pulls from the final value of the stack and removes it.
            j += 1
