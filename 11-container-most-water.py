# https://leetcode.com/problems/container-with-most-water/
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.

#Input: height = [1,8,6,2,5,4,8,3,7]
#Output: 49
#Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Time: O(n^2)
# Space: O(1)
# Time limit exceeded
class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxA = 0

        for i, v1 in enumerate(height):
            for j, v2 in enumerate(height[i:]):
                maxA = max(maxA, (i+j - i) * min(v1, v2))
        return maxA

# Time optimized
# Time: O(n) Single pass
# Space: O(1)
# Have 2 pointers starting at left most and right most.
# Calculate area with min of v1 and v2
# Move pointer closer by removing the smallest of v1 and v2, its increases the area
class Solution1:
    def maxArea(self, height: list[int]) -> int:
        maxA = 0
        i = 0
        j = len(height) - 1
        
        while i < j:
            maxA = max(maxA, (j-i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i = i + 1
            else:
                j = j - 1

        return maxA