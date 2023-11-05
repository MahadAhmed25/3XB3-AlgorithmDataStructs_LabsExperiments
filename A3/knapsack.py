import random

def create_knapsack(numItems, lowerWeight, upperWeight, lowerValue, UpperValue):
    sack = set()
    while len(sack) < numItems:
        weight = random.randint(lowerWeight, upperWeight)
        value = random.randint(lowerValue, UpperValue)
        sack.add(tuple((weight,value)))
    return list(sack)
        
    

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
    return True

def ks_top_down(sack, capacity):
    return True
    
    
    
#Example code to create a knapsack
x = create_knapsack(10, 1, 10, 1, 10)
print(x)
print("------------------")
print(ks_rec(x, 7))
