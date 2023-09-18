import random
import timeit
import matplotlib.pyplot as plot

def swap(L, i, j):
    L[i], L[j] = L[j], L[i]

#Iterative binsearch, returns True iff value is in values
def binsearch1(value, values):
    left, right = 0, len(values) - 1
    while left < right:
        mid = (left + right)//2
        if values[mid] == value:
            return True
        if values[mid] < value:
            left = mid + 1
        else:
            right = mid
    return values[left] == value

def binsearch2(value, values):
    left, right = 0, len(values) - 1
    while left != right:
        mid = (left + right) // 2
        if values[mid] < value:
            left = mid + 1
        elif values[mid] > value:
            right = mid
        else:
            return True
    return values[left] == value

def binsearch3(value, values):
    return binsearch_rec(value, values, 0, len(values) - 1)

def binsearch_rec(value, values, left, right):
    if values == []:
        return False
    if left == right:
        return values[left] == value
    mid = (left + right) // 2
    if values[mid] < value:
        return binsearch_rec(value, values, mid+1, right)
    elif values[mid] > value:
        return binsearch_rec(value, values, left, mid)
    else:
        return True

#Traditional insertion sort
def insertion_sort(L):
    for i in range(1, len(L)):
        insert(L, i)


def insert(L, i):
    while i > 0:
        if L[i] < L[i-1]:
            L[i], L[i-1] = L[i-1], L[i]
            i -= 1
        else:
            return

def insertion_sort3(L):
    for i in range(1, len(L)):
        j = i
        while j > 0:
            if L[j] < L[j - 1]:
                L[j], L[j - 1] = L[j - 1], L[j]
                j -= 1
            else:
                break

def insertion_sort2(L):
    for i in range(1, len(L)):
        insert2(L, i)


def insert2(L, i):
    value = L[i]
    while i > 0:
        if L[i - 1] > value:
            L[i] = L[i - 1]
            i -= 1
        else:
            L[i] = value
            return
    L[0] = value


def create_random_list(length, max_value):
    L = []
    for _ in range(length):
        L.append(random.randint(0, max_value))
    return L

# ******************* Selection sort code *******************

# Traditional Selection sort
def selection_sort(L):
    for i in range(len(L)):
        min_index = find_min_index(L, i)
        swap(L, i, min_index)


def find_min_index(L, n):
    min_index = n
    for i in range(n+1, len(L)):
        if L[i] < L[min_index]:
            min_index = i
    return min_index


# ****************** Solutions ******************
def selection_sort2(L):
    for i in range(len(L) // 2):
        min_index = i
        max_index = len(L) - i - 1
        for j in range(i+1, len(L)-i):
            if L[j] < L[min_index]:
                min_index = j
            elif L[j] > L[max_index]:
                max_index = j
        if min_index != len(L) - i:
            swap(L, i, min_index)
        swap(L, len(L) - i - 1, max_index)

def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                swap(L, j, j+1)

def bubble_sort2(L):
    for i in range(len(L)):
        value = L[0]
        for j in range(len(L) - 1):
            if value > L[j + 1]:
                L[j] = L[j + 1]
            else:
                L[j] = value
                value = L[j+1]


total1 = 0
total2 = 0
total3 = 0
n = 1000
for _ in range(n):
    L = create_random_list(1000, 10000)
    L.sort()

    start = timeit.default_timer()
    binsearch1(5000, L)
    total1 += timeit.default_timer() - start

    start = timeit.default_timer()
    binsearch2(5000, L)
    total2 += timeit.default_timer() - start

    start = timeit.default_timer()
    binsearch3(5000, L)
    total3 += timeit.default_timer() - start


print("Method 1: ", total1/n)
print("Method 2: ", total2/n)
print("Method 3: ", total3/n)
print("Method 2 takes " + str(total2/total1) + " the amount of time Method 1 does.")
print("Method 3 takes " + str(total3/total1) + " the amount of time Method 1 does.")


"""
total1 = 0
total2 = 0
total3 = 0
data = []
n = 10
k = 500

for _ in range(n):
    L = create_random_list(k, k)
    L2 = L.copy()

    start = timeit.default_timer()
    bubble_sort(L)
    end = timeit.default_timer()
    total1 += end - start

    start = timeit.default_timer()
    bubble_sort2(L2)
    end = timeit.default_timer()
    total2 += end - start


print("Method 1: ", total1/n)
print("Method 2: ", total2/n)
print("Improvement of ", (1 - total2/total1) * 100, "%")
#print("Method 3: ", total3/n)
"""











"""
runs = 1000000
total_time = 0
for _ in range(runs):
    start = timeit.default_timer()
    n = 0
    for i in range(10):
        n += i
    end = timeit.default_timer()
    total_time += end - start
print(total_time/runs)

"""














"""
total_time = 0

runs = 100000
for _ in range(runs):
    n = 0
    start = timeit.default_timer()
    for i in range(10):
        n += i
    end = timeit.default_timer()
    total_time += end - start
print(total_time/runs)
"""




"""
total1 = 0
total2 = 0
n = 1000
for _ in range(n):
    L = create_random_list(1000, 1000)

    start = timeit.default_timer()
    binsearch1(500, L)
    total1 += timeit.default_timer() - start

    start = timeit.default_timer()
    binsearch2(500, L)
    total2 += timeit.default_timer() - start


print("Method 1: ", total1/n)
print("Method 2: ", total2/n)

"""



"""
def binsearch1(value, values):
    left, right = 0, len(values) - 1
    while left < right:
        mid = (left + right) // 2
        if values[mid] == value:
            return True
        if values[mid] < value:
            left = mid + 1
        else:
            right = mid
    return values[left] == value


def binsearch2(value, values):
    left, right = 0, len(values) - 1
    while left != right:
        mid = (left + right) // 2
        if values[mid] < value:
            left = mid + 1
        elif values[mid] > value:
            right = mid
        else:
            return True
    return values[left] == value

def binsearch3(value, values):
    return binsearch_rec(value, values, 0, len(values) - 1)

def binsearch_rec(value, values, left, right):
    if values == []:
        return False
    if left == right:
        return values[left] == value
    mid = (left + right) // 2
    if values[mid] < value:
        return binsearch_rec(value, values, mid+1, right)
    elif values[mid] > value:
        return binsearch_rec(value, values, left, mid)
    else:
        return True
        

def insertion_sort2(L):
    for i in range(1, len(L)):
        insert2(L, i)


def insert2(L, i):
    value = L[i]
    while i > 0:
        if L[i - 1] > value:
            L[i] = L[i - 1]
            i -= 1
        else:
            L[i] = value
            return
    L[0] = value

def create_random_list(length, max_value):
    L = []
    for _ in range(length):
        L.append(random.randint(0, max_value))
    return L

"""