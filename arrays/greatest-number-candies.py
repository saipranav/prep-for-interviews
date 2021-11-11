# There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
# Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
# Note that multiple kids can have the greatest number of candies.
# Constraints:

# n == candies.length
# 2 <= n <= 100
# 1 <= candies[i] <= 100
# 1 <= extraCandies <= 50
class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        m = -1
        r = []
        
        for i in candies:
            if m < i:
                m = i
 
        m = m - extraCandies
        
        for i in candies:
            if i >= m:
                r.append(True)
            else:
                r.append(False)

        return r

print(Solution().kidsWithCandies([2,5,1,3,4,7], 3)) # [false, true, false, false, false, true]