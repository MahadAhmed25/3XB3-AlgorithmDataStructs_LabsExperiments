import random

def create_knapsack(numItems, lowerWeight, upperWeight, lowerValue, UpperValue):
    sack = set()
    while len(sack) < numItems:
        weight = random.randint(lowerWeight, upperWeight)
        value = random.randint(lowerValue, UpperValue)
        sack.add(tuple((weight,value)))
    return list(sack)

def print_matrix(matrix):

    for row in matrix:
        for element in row:
            print(f"{element:4}", end=" ")
        print()
        
    

def ks_brute_force(sack, capacity):
    return True

def ks_rec(sack, capacity):
    i = len(sack)
    
    if i == 0 or capacity == 0:
        return 0
    
    if sack[i-1][0] > capacity:
        return ks_rec(sack[:-1], capacity)
    else:
        return max(ks_rec(sack[:-1], capacity), ks_rec(sack[:-1], capacity-sack[i-1][0]) + sack[i-1][1])

def ks_bottom_up(sack, capacity):
    matrix = [[0 for j in range(capacity + 1)] for i in range(len(sack) + 1)]
    
    for i in range(1, len(sack) + 1):
        for j in range(1, capacity + 1):
            
            if sack[i-1][0] > j:
                matrix[i][j] = matrix[i - 1][j]
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i - 1][j - sack[i-1][0]] + sack[i-1][1])
        
    print_matrix(matrix)             
    return matrix[len(sack)][capacity]

def ks_top_down(sack, capacity):
    return True
    
    
    
#Example code to create a knapsack
x = create_knapsack(10, 1, 10, 1, 10)
print(x)

y = ks_bottom_up(x, 20)
print(y)
