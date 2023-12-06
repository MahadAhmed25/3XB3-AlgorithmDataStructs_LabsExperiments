# source used for help: https://www.geeksforgeeks.org/egg-dropping-puzzle-dp-11/
def bsp_value(L, m):
    n = len(L)

    # dp[i][j] stores max minimum distance for first i stations with j stations removed
    dp = [[0 for _ in range(m+1)] for _ in range(n)]

    # Fill table for base cases
    for i in range(1, n):
        dp[i][0] = L[i] - L[i-1]

    # fillng table
    for j in range(1, m+1):
        for i in range(1, n):
            dp[i][j] = float('inf')
            for k in range(1, i+1):
                # check distance if kth station is removed
                if i > k:
                    dp[i][j] = min(dp[k-1][j-1], L[i] - L[k])

    # nswer is max of the minimum distances
    return max(dp[-1])


def bsp_solution(L, m):
    max_diff = bsp_value(L, m)
    last_station_kept = L[0]
    result = [last_station_kept]

    # Lopp through stations from 1st index (2nd station)
    for station in L[1:]:
        # if current station is far enough from last kept station according to calculated max_diff
        if station - last_station_kept >= max_diff:
            # Add station to result list
            result.append(station)
            # Update last kept station
            last_station_kept = station

    # returning final list of stations after potentially removing some stations
    return result

print(bsp_value([2, 4, 6, 7, 10, 14], 2)) # result should be 4
print(bsp_solution([2, 4, 6, 7, 10, 14], 2)) # Solution should be [2,6,10,14]