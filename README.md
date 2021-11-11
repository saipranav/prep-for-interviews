# prep-for-interviews
interview questions | coding categorized | system level 

## Math concepts
---
### To store 2 numbers in same place
If you want to store 2 numbers n1, n2 in to same number

consider a larger number c thats greater than n1 and n2

you can store v = (c * n1) + n2

to retrieve first number n1 = v / c ( divide )

to retrive second number n2 = v % c ( modulo )

Example:

```
n1 = 4 and n2 = 5 and c = 10
v = (10 * 4) + 5 = 45
cal n1 = int( v / c ) =  int ( 45 / 10 ) = int ( 4.5 ) = 4
cal n2 = v % c = 45 % 10 = 5
```
---

### To find number of unique combinations of pairs given an array
```
n               n!
 C     =   -------------
  r         r! * (n-r)!
```
Example find unique pairs (2 elements) from a set of 5 elements

5 C 2 = 10

In python 

1. you can have math.comb(n, r) = number of combinations

2. you can have math.factorial(n) // math.factorial(r) // math.factorial(n-r) where // is integer division for not overflowing

3. you can import itertools to get all combinations

    for comb in itertools.combinations([1, 2, 3, 4, 5], 2):
        print(comb)

### Sum of n numbers starting from 0 .. 1 .. N-1 .. N

Sum(n) = ( N * (N-1) ) / 2
