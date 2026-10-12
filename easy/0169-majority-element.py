# 169. Majority Element
# Difficulty: Easy
# https://leetcode.com/problems/majority-element/
# Runtime: 1 ms | Memory: 21.5 MB

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
