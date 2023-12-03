def bsp_value(L, m):

    def is_feasible(mid):
        removed_elements, last = 0, L[0]
        for i in range(1, len(L)):
            if L[i] - last < mid:
                removed_elements += 1
            else:
                last = L[i] # update last because this eleemnt not removed
            
            if removed_elements > m:
                return False # can return false becasue if more than m elements removed => mid is not feasible
        return True

    # Doing a binary search to find max feasible distance
    low, high = 0, L[-1] - L[0]
    while low < high:
        mid = (low + high + 1) // 2 # midpoint
        if is_feasible(mid): # if feasible distance then we can move the lower bound up
            low = mid
        else: # else decrease upper bound
            high = mid - 1
    return low


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