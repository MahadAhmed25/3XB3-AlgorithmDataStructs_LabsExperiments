# https://www.geeksforgeeks.org/python-program-for-egg-dropping-puzzle-dp-11/

# Base Cases
# if m = 1, then dp(m, n) = n (where num_of_wc_runs(m, n) is min num of tests needed for m bricks and n force settings)
# if n = 1, then dp(m, n) = 1
# if n = 0 or m = 0, then dp(m, n) = 0

# Recursive (Finding minimum number of attempts needed to determine the highest safe force setting)
# dp[i][j] = min((max(dp[i-1][k-1], dp[i][j-k]) + 1) for k in range(1, j+1))


def num_of_wc_runs(n, m):
    # n - number of force settings, m - number of bricks

    # make the table holding results fo subproblems
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
 
    # Base case:
    for i in range(1, m + 1):
        dp[i][1] = 1
        dp[i][0] = 0

    for j in range(1, n + 1):
        dp[1][j] = j
 
    # Fill table
    for i in range(2, m + 1):
        for j in range(2, n + 1):
            dp[i][j] = min((max(dp[i-1][k-1], dp[i][j-k]) + 1) for k in range(1, j+1))

    return dp[m][n]


def next_setting(n, m):
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    next_k = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(1, m+1):
        dp[i][0] = 0
        dp[i][1] = 1
        next_k[i][0] = 0
        next_k[i][1] = 1 

    for j in range(1, n+1):
        dp[1][j] = j
        next_k[1][j] = 1  # with 1 brick, we should always start from 1

    for i in range(2, m+1):
        for j in range(2, n+1): 
            dp[i][j] = min((max(dp[i-1][k-1], dp[i][j-k]) + 1) for k in range(1, j+1))

            wc = float('inf')
            for k in range(1, j+1):
                res = 1 + max(dp[i-1][k-1], dp[i][j-k])
                if res < wc:
                    wc = res
                    next_k[i][j] = k

    return next_k[m][n]


print(num_of_wc_runs(100, 2))
print(next_setting(100, 2))
