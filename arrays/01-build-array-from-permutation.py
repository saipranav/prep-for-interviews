# Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

# Constraints:
# 1 <= nums.length <= 1000
# 0 <= nums[i] < nums.length
# The elements in nums are distinct.

# O(n)
class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        ans = list[int]()
        for i in nums: # loops every element and consider value as index to get actual value
            ans.append(nums[i])
        return ans

print(Solution().buildArray(nums=[0,2,1]))