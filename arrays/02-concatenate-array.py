# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
# Constraints:
# n == nums.length
# 1 <= n <= 1000
# 1 <= nums[i] <= 1000

# this seems the optimized version but nope, uses little bit more memory than next solution same time
class Solution1:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums + nums

print(Solution1().getConcatenation(nums=[1,2,3]))


# optimized - memory allocation is done at start
# O(n)
class Solution2:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        l = len(nums)
        ans = [0] * ( l * 2 )
        for i in range(l):
            ans[i] = nums[i]
            ans[i+l] = nums[i]
        return ans

print(Solution2().getConcatenation(nums=[1,2,3]))

