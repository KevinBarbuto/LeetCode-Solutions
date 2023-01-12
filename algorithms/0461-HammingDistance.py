# Objective: Return the hamming distance between two integers.

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y # XOR to find differences
        binary = "{0:b}".format(xor) # convert int to bin

        # add binary bits together
        sum = 0
        for bit in binary:
            sum += int(bit)

        return sum
