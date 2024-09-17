# Objective: Take an array of integers and a target integer, and
# find the indices of the array such that they add up to the target

# For this version of the problem, I attempted a solution that is based around
# comparing each value in the array to a dictionary of the previous values.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # hash table of previous values in array

        for i, n in enumerate(nums):
            diff = target - n # difference between target int and current val
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
