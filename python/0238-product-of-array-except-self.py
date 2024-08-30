# Objective: Given an array, create another array in which each element
# is the product of all of the original array's elements except for 
# the one at the same index.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Starting values
        result = [1] * len(nums) # result array
        pre = 1
        post = 1

        # prefix array
        for i in range( len(nums) ):
            result[i] = pre
            pre *= nums[i]
        
        # postfix array
        for i in range( len(nums)-1, -1, -1 ):
            result[i] *= post
            post *= nums[i]

        return result
