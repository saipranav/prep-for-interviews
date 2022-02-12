# https://leetcode.com/problems/3sum-smaller/
# Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

# Time: O(n^2) outer p1, then 2 pointer loop
# Space: O(n) sorting
# Approach: fix 1 element, then continue with two pointer l = i + 1 and r = last index
#           when the sum is less than target, increment res but you can increment a lot at once (because all elements were sorted)
#           so i,j,k and i,j,k-1 all these are going to be valid hence r-l combinations
#           then increment l so that we move to i,j+1,k combinations
#           in case target is more than sum then shrink using r pointer as much as needed
class Solution:
    def threeSumSmaller(self, nums: list[int], target: int) -> int:
        nums.sort()
        res = 0
        
        for i, p1 in enumerate(nums):
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < target:
                    res = res + (r - l)
                    l = l + 1
                else:
                    r = r - 1

        return res