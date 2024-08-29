# Objective: Find the bitwise complement (logical NOT) of an input integer.

class Solution:
    def findComplement(self, num: int) -> int:
        complement = "" # dummy string

        # replace each byte with its opposite
        for i in bin(num)[2:]: # convert num to binary, ignore 0b
            if i is "0":
                complement += "1"
            else:
                complement += "0"
        
        return int(complement,2) # converts from base-2 value back to integer
