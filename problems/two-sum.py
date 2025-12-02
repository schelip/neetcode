"""
Two Sum

Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:

Input: nums = [4,5,6], target = 10

Output: [0,2]
Example 3:

Input: nums = [5,5], target = 10

Output: [0,1]
Constraints:

2 <= nums.length <= 1000
-10,000,000 <= nums[i] <= 10,000,000
-10,000,000 <= target <= 10,000,000
Only one valid answer exists.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        core concept: hash maps
        brute force complexity: check every pair of elements - O(n^2)
        target complexity: O(n)

        For each element, we need to check if the difference to the target is also in the array.
        By using a hash map, mapping the visited values to the index it was found, we can do this in O(1).
        """
        visited = {nums[0]: 0}

        for j in range(1, len(nums)):
            difference = target - nums[j]

            if difference in visited:
                return [visited[difference], j]

            visited[nums[j]] = j
