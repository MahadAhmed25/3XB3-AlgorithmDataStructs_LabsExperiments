import math

'''
Recursion:

n := range of forces from 1 to n
m := number of bricks

let brickTest(m,n) := min # of tests to find threshold force k* where brick breaks

if we have 1 brick left we must perform linear search to find k* therefore worst case would be O(n-1):
brickTest(1,n) = n - 1

if we have as many bricks as searches for the binary search (ie. m >= log2(n) + 1) then we can perform binary search and find k*:
brickTest(m,n) = log2(n)   if m >= log2(n) + 1
'''

def brickTest_rec(m,n):
    if m < 1 or n < 1:
        return 0
    
    if m == 1:
        return n - 1

    if m >= math.log(n,2) + 1:
        return math.log(n,2)

n = 100
m = 2
print("Minimum Tests Required To Find Threshold Force For Brick Breaking: ", brickTest_rec(m,n))
        