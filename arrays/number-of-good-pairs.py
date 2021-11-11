# Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.
# Constraints:
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100

# O(n)
# O(n)
import math
class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        m = {}
        r = 0

        for i, v in enumerate(nums):
            if v in m:
                m[v] = m[v]+1
            else:
                m[v] = 1

        for k, v in m.items():
            if v < 1:
                continue
            r = r + math.comb(v, 2)

        return r

print(Solution().numIdenticalPairs([1,2,3,1,1,3])) # 4

# O(n)
# without calling combinations because we can calculate number of pairs since we are starting to count the number of occurences
class Solution1:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        m = {}
        r = 0

        for i, v in enumerate(nums):
            if v in m:
                m[v] = m[v]+1
            else:
                m[v] = 0

            r = r + m[v]
        return r
print(Solution1().numIdenticalPairs([1,2,3,1,1,3])) # 4
