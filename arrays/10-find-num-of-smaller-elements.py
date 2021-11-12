# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
# Constraints:
# 2 <= nums.length <= 500
# 0 <= nums[i] <= 100

# O(n^2)
# O(n)
class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        r = [0]*len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    r[i] = r[i] + 1

        return r
print(Solution().smallerNumbersThanCurrent([8,1,2,2,3])) # [4,0,1,1,3]

# O(nlogn) because of efficient sorting
# O(n) space
# way more efficient in terms of runtime
# sort the list and get the index of each element, it gives the required info of how many elements are smaller than current element 
class Solution1:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        r = []
        s = list(nums)
        s.sort()

        # takes first found index number of each value from sorted list
        # this gives how many elements are present before current element because its sorted 
        m = {}
        for i, v in enumerate(s):
            if v not in m:
                m[v] = i

        for v in nums:
            r.append(m[v])

        return r
print(Solution1().smallerNumbersThanCurrent([8,1,2,2,3])) # [4,0,1,1,3]