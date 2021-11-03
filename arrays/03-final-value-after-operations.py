# There is a programming language with only four operations and one variable X:
# ++X and X++ increments the value of the variable X by 1.
# --X and X-- decrements the value of the variable X by 1.
# Initially, the value of X is 0.

# Constraints:

# 1 <= operations.length <= 100
# operations[i] will be either "++X", "X++", "--X", or "X--".

# O(n)
class Solution1:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        x = int(0)
        for op in operations: # loop every operation atleast once to find what we need to do
            if op[1] == "+": # second index char gives + or - ; reducing the number of ifs required to 1
                x = x + 1
            else:
                x = x - 1
        return x

print(Solution1().finalValueAfterOperations(["x++", "--x"]))

# O(n)
# I like this solution because you can extend it than adding another if clause but there are some holes in this when we extend the problem
class Solution2:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        op_dict = {
            "--X" : -1,
            "X--" : -1,
            "++X" : 1,
            "X++" : 1
        }
        return sum(op_dict[op] for op in operations)

print(Solution2().finalValueAfterOperations(["x++", "--x"]))