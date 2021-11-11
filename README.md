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
