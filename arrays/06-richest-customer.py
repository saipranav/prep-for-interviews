# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.
# Constraints:
# m == accounts.length
# n == accounts[i].length
# 1 <= m, n <= 50
# 1 <= accounts[i][j] <= 100

# O(n^2)
# we need to run through each customer's all bank accounts to find the richest customer
class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        w1 = 0
        for c in accounts:
            if w1 < sum(c):    # having sum([]) function or having for loop has minimum impact on runtime
                w1 = sum(c)

        return w1

