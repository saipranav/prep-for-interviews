# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Constraints:
# 1 <= nums.length <= 1000
# -10^6 <= nums[i] <= 10^6

# O(n)
# readable and way faster, consumes less memory
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        s = 0
        r = []
        for i in nums:
            s = s + i
            r.append(s)

        # for i in range(len(nums)): # this for loop runs slower
        #     s = s + nums[i]
        #     r.append(s)

        return r
print(Solution().runningSum([1,2,3,4]))

# O(n)
# this is an unreadable solution but has list comprehension with function
s = 0
def sum(x: int) -> int:
    global s # global var  is needed otherwise python picks up local variable and complains its not assigned
    s = x+s
    return s

class Solution1:
    def runningSum(self, nums: list[int]) -> list[int]:
        global s
        s = 0
        return [sum(x) for x in nums] # list comprehension [expr with element for element in array] forms a new array
print(Solution1().runningSum([1,2,3,4]))