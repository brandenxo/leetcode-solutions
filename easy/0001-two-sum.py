# 1. Two Sum
# Difficulty: Easy
# https://leetcode.com/problems/two-sum/
# Runtime: 0 ms | Memory: 20.6 MB

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        num_map = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if the complement exists in the dictionary
            if complement in num_map:
                return [num_map[complement], i]
            
            # Store the current number and its index
            num_map[num] = i
        
        return []
