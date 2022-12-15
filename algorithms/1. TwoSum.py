# Objective: Given an input of an array and an integer, determine the indices of the two values in the array that will add up to the integer.
# Constraint: Assume only one valid solution.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        currentMap = {} # difference : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in currentMap: # tests the current value against previous ones
                return [ currentMap[diff], i ] # prints
            currentMap[n] = i # Sets current value in hash table
        return
