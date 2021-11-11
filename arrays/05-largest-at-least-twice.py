# You are given an integer array nums where the largest integer is unique.
# Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.

# Constraints:
# 1 <= nums.length <= 50
# 0 <= nums[i] <= 100
# The largest element in nums is unique

# O(n)
# This solution works perfectly because from constraints we know the numbers in array are not going to be negative so we can initialize l1 with -1
# Tricky test cases:
# [1]
# [1, 0]
# [0, 1]
class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        idx = l1 = l2 = -1
        for i, v in enumerate(nums):
            if l1 <= v:
                idx, l1, l2 = i, v, l1  
            elif l2 <= v:
                l2 = v

        if l2 * 2 <= l1:
            return idx
        else:
            return -1
print(Solution().dominantIndex([1,2,3,4])) # -1
print(Solution().dominantIndex([1,0])) # 0
