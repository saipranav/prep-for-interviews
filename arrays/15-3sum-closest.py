# https://leetcode.com/problems/3sum-closest/
# Time: O(n^2) p1 outer loop then two pointer while loop
# Space: O(n) sorting
# Approach: fix 1 element, have 2 pointers on rest
#           Since we dont have a target, aim for smallest difference between target and tempSum
#           If tempSum < target, it means we can grow so increment left pointer
#           If tempSum > target, it means we need to shrink so decrement right pointer
#           In two pointer loop, keep track of closest with absolute difference between target and tempSum
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest = 0
        closestDiff = float('inf')
        
        for i, p1 in enumerate(nums):
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                tempSum = p1 + nums[l] + nums[r]
                if closestDiff > abs(target - tempSum):
                    closestDiff = abs(target - tempSum)
                    closest = tempSum
                if target < tempSum:
                    r = r - 1
                elif target > tempSum:
                    l = l + 1
                else:
                    closestDiff = (target - tempSum)
                    closest = tempSum
                    l = l + 1

        return closest