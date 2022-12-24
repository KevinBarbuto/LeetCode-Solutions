# Objective: Given an input of an array and an integer, determine the indices of the two values in the array that will add up to the integer.
# Constraint: Assume only one valid solution.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        return i,j
