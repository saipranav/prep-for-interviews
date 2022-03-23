# https://leetcode.com/problems/4sum/
# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.


class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        res = set()
        
        if len(nums) < 4:
            return res
        
        for i, p1 in enumerate(nums):
            for j, p2 in enumerate(nums[i+1:]):
                l = i + 1 + j + 1
                r = len(nums) - 1
                
                while l < r:
                    s = p1 + p2 + nums[l] + nums[r]
                    if s > target:
                        r = r - 1
                    elif s < target:
                        l = l + 1
                    else:
                        res.add(tuple(sorted([p1, p2, nums[l], nums[r]])))
                        l = l + 1
        
        return res