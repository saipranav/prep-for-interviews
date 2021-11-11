# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

# Constraints:
# 1 <= n <= 500
# nums.length == 2n
# 1 <= nums[i] <= 10^3

# O(n) 
# space new 2n array
# have 2 pointers with n elements apart and place them in new array like a zipper
class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        res = []
        x = 0
        y = n
        
        for i in range(n):
            res.append(nums[x])
            res.append(nums[y])
            x = x+1
            y = y+1
        
        return res

print(Solution().shuffle([1,2,3,4], 2)) # [1,3,2,4]

# time: O(n)
# space: O(n) at most n/2 elements on queue
# In place shuffle
class Solution1:
    def shuffle(self, nums: list[int], n: int) -> list[int]:  
        y = n    # second pointer
        q = []   # empty queue

        for x in range(2*n):           # first pointer

            if x == 0 or x == 2*n-1:   # don't disturb first and last element
                continue

            q.append(nums[x])          # placing current element in queue because we are replacing first pointer `nums[x]` in both cases below so we need somewhere to temporarily store
			
            if x % 2 == 0:             # even index, get first element from queue
                nums[x]=q.pop(0)
            else:                      # odd index, swap element with second pointer and increment second pointer
                nums[x]=nums[y]
                y = y + 1


        return nums
print(Solution1().shuffle([2,5,1,3,4,7], 3)) # [2,3,5,4,1,7]

# from submission, kudos to @yuanzhi247012 https://leetcode.com/problems/shuffle-the-array/discuss/675007/Python-O(n)-time-O(1)-space-detailed-explanation
# O(n^2)
# O(1) even without queue
# first of all he found the logic for desired index
# negates when the desired position is filled correctly
# loops in same place until the current index is having a negated value because if we move to another loop iteration then places gets changed
class Solution2:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        getDesireIdx = lambda i: i*2 if i<n else (i-n)*2+1
        for i in range(2*n):
            j=i
            while nums[i]>=0:
                j=getDesireIdx(j)
                nums[i],nums[j]=nums[j],-nums[i]
        for i in range(2*n):
            nums[i]=-nums[i]
        return nums
print(Solution2().shuffle([2,5,1,3,4,7], 3)) # [2,3,5,4,1,7]

# This is a way better solution but works for this constraints which each number is under 1000
# O(n)
# O(1) in place space
# This creatively uses basic math divide.
# If you want to store 2 numbers n1, n2 in to same number
#  consider a larger number c thats greater than n1 and n2
#    you can store v = (c * n1) + n2
#    to retrieve first number n1 = v / c ( divide )
#    to retrive second number n2 = v % c ( modulo )
# such a neat concept kudos to @mettleap https://leetcode.com/problems/shuffle-the-array/discuss/909259/Java-In-place-O(n)-Time-and-O(1)-space
class Solution3:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        c = 1001 # since elements are not going to be greater than 1000

        for i in range(n, 2*n):
            nums[i] = c*nums[i-n]+nums[i]
            
        idx = 0
        for i in range(n, 2*n):
            nums[idx] = int(nums[i]/c)
            nums[idx+1] = nums[i]%c
            idx = idx + 2

        return nums
print(Solution3().shuffle([2,5,1,3,4,7], 3)) # [2,3,5,4,1,7]