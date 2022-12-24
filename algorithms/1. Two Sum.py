# Objective: Given an input of an array and an integer, determine the indices of the two values in the array that will add up to the integer.
# Constraint: Assume only one valid solution.

# Note: This probably isn't the most optimal to this problem, as it brute-force searches the entire list. 
# If I were to optimize this, I would probably write it to compare the target with each entry in the list so that the code doesn't have to potentially search through the entire list twice.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        return i,j
