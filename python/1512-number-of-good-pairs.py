class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums = sorted(nums)
        dict = {}
        answer = 0

        for i in range(len(nums)-1): # Iterate through lists and set dictionary values
            if nums[i] == nums[i+1]:
                if nums[i] not in dict:
                    dict[nums[i]] = 1
                dict[nums[i]] = dict[nums[i]] + 1
        
        for x in dict.values(): # Apply quadratic sequence
            answer += (x**2 - x) // 2
        
        return answer
