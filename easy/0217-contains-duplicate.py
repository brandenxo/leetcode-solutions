# 217. Contains Duplicate
# Difficulty: Easy
# https://leetcode.com/problems/contains-duplicate/
# Runtime: 18 ms | Memory: 32.2 MB

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num not in seen:
                seen.add(num)
            elif num in seen:
                return True
        return False
