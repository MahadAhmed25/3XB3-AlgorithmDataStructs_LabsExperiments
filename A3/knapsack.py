from itertools import combinations
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
        
    
#https://towardsdev.com/knapsack-problem-brute-force-solution-40d2e2deaacd reference of algorithm, it was a direct implmentation
def ks_brute_force(sack, capacity):
    length = len(sack)
    max_value = 0
    brute_comb = []

    for i in range (1, length+1):
        for combination in combinations(range(length), i):
            total_weight = sum(sack[i][0] for i in combination)
            total_value = sum(sack[i][1] for i in combination)

            if total_weight <= capacity and total_value > max_value:
                max_value = total_value

    return max_value

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
        
    #print_matrix(matrix)             
    return matrix[len(sack)][capacity]

def ks_top_down(sack, capacity):
    sp ={}
    
    for i in range(len(sack) + 1):
        sp[(i,0)] =0
    
    for j in range(capacity + 1):
        sp[(0,j)] =0

    top_down_aux(sack, len(sack), capacity, sp)
    
    #print_matrix(sp)
    return sp[len(sack),capacity]

def top_down_aux(sack, i, j, sp):
    if sack[i-1][0] > j:
        if (i - 1, j) not in sp:
            top_down_aux(sack, i - 1, j, sp)
        sp[i,j] = sp[i - 1,j] 
    
    else:
        if (i - 1, j) not in sp:
            top_down_aux(sack, i - 1, j, sp)
            
        if (i - 1, j - sack[i - 1][0]) not in sp:
            top_down_aux(sack, i - 1, j - sack[i-1][0], sp)

        sp[i,j] = max(sp[i - 1, j], sp[i - 1, j - sack[i-1][0]] + sack[i-1][1])
    
    
#Example code to create a knapsack
x = create_knapsack(10, 1, 10, 1, 10)
#print(x)

t = ks_bottom_up(x, 20)
print(t)

y = ks_top_down(x, 20)
print(y)

z=ks_brute_force(x,20)
print(z)

