# Base Cases
# if m = 1, then num_of_wc_runs(m, n) = n (where num_of_wc_runs(m, n) is min num of tests needed for m bricks and n force settings)
# if n = 1, then num_of_wc_runs(m, n) = 1
# if n = 0 or m = 0, then num_of_wc_runs(m, n) = 0

# Recursive (Finding minimum number of attempts needed to determine the highest safe force setting)
# num_of_wc_runs(m,n) = min(max(num_of_wc_runs(m-1, k-1), num_of_wc_runs(m, n-k))) for k in range(1, j+1)

def num_of_wc_runs(n, m):
    # n - number of force settings, m - number of bricks

    # make the table holding results fo subproblems
    brickTest = [[0 for _ in range(n+1)] for _ in range(m+1)]
 
    # Base case: if 1 brick, we test each force setting 
    for i in range(1, m + 1):
        brickTest[i][1] = 1
        brickTest[i][0] = 0
 
    for j in range(1, n + 1):
        brickTest[1][j] = j
 
    # Fill table
    for i in range(2, m + 1):
        for j in range(2, n + 1):
            brickTest[i][j] = float('inf')
            # considering all possible first moves (testing brick at each force setting k)
            # 1. brick breaks, we have 1 less brick and k-1 remaining force settings to test
            # 2. brick doesnt break and we still have all bricks and j-k force settings left to test
            for k in range(1, j + 1):
                wc = 1 + max(brickTest[i-1][k-1], brickTest[i][j-k])

                # if this move has lower worst case than current best we needa update it
                if wc < brickTest[i][j]:
                    brickTest[i][j] = wc
 
    # last element in tbae is min num of test needed for m bricks and n force settings
    return brickTest[m][n]


def next_setting(n, m):
    pass



print(num_of_wc_runs(100, 2))
# print(next_setting(100, 2))
