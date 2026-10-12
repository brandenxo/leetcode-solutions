# 169. Majority Element
# Difficulty: Easy
# https://leetcode.com/problems/majority-element/
# Runtime: 26 ms | Memory: 21.6 MB

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency = {}

        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] += 1
        return max(frequency, key=frequency.get)
