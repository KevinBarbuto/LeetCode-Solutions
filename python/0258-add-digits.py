# Objective: Return the digital root of a given num.

class Solution:
    def addDigits(self, num: int) -> int:
        if num <= 9: # for one-digit num
            return num

        tot = 0 # final tally will be added here

        while num > 0:
            tot += num % 10 # mod to add smallest digit
            num = num // 10 # get rid of smallest digit
        return self.addDigits(tot) # recursion for when tot is still 2 or more digits
