# https://leetcode.com/problems/two-sum-iii-data-structure-design/
# Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.

# Time O(nlogn) <- sorting 
# Space O(n) <- saving array
# Approach: sort the numbers at first find and again when we update array.
# With sorted array have two pointers and take sum, see if the sum is greater or lesser. If lesser then increase the left pointer, if greater decrese the right pointer
class TwoSum:
    arr = []
    sorted = False

    def __init__(self):
        self.arr = []
        self.sorted = False

    def add(self, number: int) -> None:
        self.arr.append(number)
        self.sorted = False

    def find(self, value: int) -> bool:
        if self.sorted == False:
            self.arr.sort()
            self.sorted = True
        
        l = 0
        r = len(self.arr) - 1
        
        while l < r:
            sum = self.arr[l] + self.arr[r]
            if sum < value:
                l = l + 1
            elif sum > value:
                r = r - 1
            else:
                return True
        return False

# Time: O(n) <- when we go through all keys in map
# Space: O(n) <- needed for map
# Approach: create map if numbers while input with each frequency. At find stage, given a target, for each key in map k1 find k2 which is ( target - k1 ) is also in map.
# special case where keeping frequency helps is when k1 and k2 are same, then check if count is > 1 
class TwoSum1:
    m = {}

    def __init__(self):
        self.m = {}

    def add(self, number: int) -> None:
        if number in self.m:
            self.m[number] = self.m[number] + 1
        else:
            self.m[number] = 1

    def find(self, value: int) -> bool:
        for key in self.m:
            if (value - key) in self.m:
                if (value - key) == key:
                    if self.m[key] > 1:
                        return True
                    else:
                        continue
                return True
        return False
        

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)