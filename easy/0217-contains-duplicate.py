# 217. Contains Duplicate
# Difficulty: Easy
# https://leetcode.com/problems/contains-duplicate/
# Runtime: 12 ms | Memory: 32.4 MB

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
