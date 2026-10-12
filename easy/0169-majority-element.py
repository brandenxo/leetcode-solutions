# 169. Majority Element
# Difficulty: Easy
# https://leetcode.com/problems/majority-element/
# Runtime: 15 ms | Memory: 21.5 MB

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency = defaultdict(int)

        for num in nums:
            frequency[num] += 1
                
        return max(frequency, key=frequency.get)
