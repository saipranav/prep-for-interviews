# https://leetcode.com/problems/two-sum-less-than-k/
# Given an array nums of integers and integer k, return the maximum sum such that there exists i < j with nums[i] + nums[j] = sum and sum < k. If no i, j exist satisfying this equation, return -1.

# Time: O(nlogn) sorting
# Space: O(n) depending on sorting
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        maxSum = -1
        nums.sort() # make possible to use two pointer approach
        
        l = 0
        r = len(nums) - 1
        
        # Optimization: find possible r value beyond which its not useful to search since the postive sorted nums
        for i, e in enumerate(nums):
            if k < e:
                r = i - 1
                break
        
        # we dont know the target, we know k
        # two pointer sum, then if sum is less than k, keep a maxSum
        # if sum is less than k then we can move closer so left pointer + 1
        # if sum is greater than k then we must fall below so right pointer - 1
        while l < r:
            s = nums[l] + nums[r]
            if s < k:
                maxSum = max(maxSum, s)
                l = l + 1
            else:
                r = r - 1       
        
        return maxSum
        