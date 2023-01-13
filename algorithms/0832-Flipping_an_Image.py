# Objective: Horizontally flip an image of binary values and invert them.

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        for line in image:
            line.reverse() # flip horizontally

            for i in range( len(line) ):
                line[i] ^= 1 # XOR operation to invert value

        return image
