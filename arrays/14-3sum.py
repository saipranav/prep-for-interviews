# https://leetcode.com/problems/3sum/
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Time O(n^2) sorting
# Space O(n) for output
# Approach: sort the numbers, for 1 fixed element from leftmost till > 0 (because after which point we are not going to arrive at target zero because its sorted)
#           given 1 element is fixed, take the complement as temporary target for two sum so it overall adds to zero
#           two sum is using two pointer, left from fixed element index + 1, right to right most. If sum of these two more than complement target then decrement right, if sum of these two are less than complement then increment left, if sum is same as complement target then we found triplet. 
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = set()

        for i, e in enumerate(nums):
            if e > 0:
                break
            self.twoSum(nums, i, res)
        
        return res
        
    def twoSum(self, nums: list[int], i: int, res: set[list[int]]):
        tSum = -1 * nums[i]
        l = i + 1
        r = len(nums) - 1
        
        while l < r:
            if nums[l] + nums[r] == tSum:
                res.add(tuple(sorted([nums[i], nums[l], nums[r]])))
                l = l + 1
            elif nums[l] + nums[r] > tSum:
                r = r - 1
            elif nums[l] + nums[r] < tSum:
                l = l + 1

# Input    [3,0,-2,-1,1,2]
# Output   [[-2,-1,3]]
# Expected [[-2,-1,3],[-2,0,2],[-1,0,1]]
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        m = {}
        r = []
        
        for e in nums:
            if e in m:
                m[e] = m[e] + 1
            else:
                m[e] = 1
        # print(m)
        found = False
        
        for e1 in m:
            if m[e1] > 0:
                m[e1] = m[e1] - 1
                
                for e2 in m:
                    if m[e2] > 0:
                        m[e2] = m[e2] - 1
                        
                        e3 = -1 * (e1 + e2)
                        if e3 in m and m[e3] > 0:
                            m[e3] = m[e3] - 1
                            sL = [e1, e2, e3]
                            sL.sort()
                            r.append(sL)
                            found = True
                        else:
                            m[e2] = m[e2] + 1
 
                if found == False:
                    m[e1] = m[e1] + 1
        
        result = []
        if len(r) == 0:
            return result

        i = 1
        r.sort()
        result.append(r[0])
        while i <= len(r)-1:
            if r[i-1] != r[i]:
                result.append(r[i])
            i = i + 1
        return result





class Solution1:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        m = {}
        r = []
        
        for e in nums:
            if e in m:
                m[e] = m[e] + 1
            else:
                m[e] = 1
        # print(m)
        
        for e1 in m:
            if m[e1] > 0:
                m[e1] = m[e1] - 1
                
                for e2 in m:
                    if m[e2] > 0:
                        m[e2] = m[e2] - 1
                        
                        e3 = -1 * (e1 + e2)
                        if e3 in m and m[e3] > 0:
                            sL = [e1, e2, e3]
                            sL.sort()
                            r.append(sL)
                            
                        m[e2] = m[e2] + 1
 
                m[e1] = m[e1] + 1
        
        result = []
        if len(r) == 0:
            return result

        i = 1
        r.sort()
        result.append(r[0])
        while i <= len(r)-1:
            if r[i-1] != r[i]:
                result.append(r[i])
            i = i + 1
        return result