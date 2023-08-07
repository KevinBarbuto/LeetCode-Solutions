# Objective: Given an integer, determine whether or not it's a palindrome (including negative signs).

class Solution:
    def isPalindrome(self, x: int) -> bool:
        first = str(x) # value to compare final result to
        newString = "" # where the palindrome goes

        for i in first [::-1]:
            newString += i
        
        if first == newString:
            return True
