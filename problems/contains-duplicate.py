"""
Contains Duplicate
Solved 
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false
"""
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        core concept: hash maps
        brute force complexity: check every pair of elements - O(n^2)
        target complexity: O(n)

        For each element, we need to check if it has already appeared in the array.
        By using a hash map, we can do this in O(1).
        """
        appeared = set()
        for i in nums:
            if i in appeared:
                return True
            appeared.add(i)
        return False
