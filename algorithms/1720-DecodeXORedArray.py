# Objective: Given an array that was created by XORing another array,
# return the original array.

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:

        result = [first] # initialize list with the first value

        # go through the rest
        for i in encoded:
            result.append(i ^ result[-1])
        
        return result
