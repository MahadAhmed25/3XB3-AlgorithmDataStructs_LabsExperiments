"""
This file corresponds to the first graded lab of 2XC3.
Feel free to modify and/or add functions to this file.
"""
import random
import time
import timeit
import matplotlib.pyplot as plt
import numpy as np


# Create a random list length "length" containing whole numbers between 0 and max_value inclusive
def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]


# Creates a near sorted list by creating a random list, sorting it, then doing a random number of swaps
def create_near_sorted_list(length, max_value, swaps):
    L = create_random_list(length, max_value)
    L.sort()
    for _ in range(swaps):
        r1 = random.randint(0, length - 1)
        r2 = random.randint(0, length - 1)
        swap(L, r1, r2)
    return L


# I have created this function to make the sorting algorithm code read easier
def swap(L, i, j):
    L[i], L[j] = L[j], L[i]


# ******************* Insertion sort code *******************

# This is the traditional implementation of Insertion Sort.
def insertion_sort(L):
    for i in range(1, len(L)):
        insert(L, i)


def insert(L, i):
    while i > 0:
        if L[i] < L[i-1]:
            swap(L, i-1, i)
            i -= 1
        else:
            return
        
# ******************* Insertion sort code VARIATION 2 *******************

def insertion_sort2(L):
    for i in range(1, len(L)):
        insert2(L, i)

def insert2(L, i):
    current_element = L[i]
    j = i - 1
    
    while j >= 0:
        if L[j] > current_element:
            L[j+1] = L[j]
            j -=1
        else:
            break
      
    L[j + 1] = current_element  



# ******************* Bubble sort code *******************

# Traditional Bubble sort
def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                swap(L, j, j+1)
                
# ******************* Bubble sort code VARIATION 2 *******************

def bubble_sort2(L):
    for i in range(len(L)):
        value = L[0]
        for j in range(len(L) - 1):
            if value > L[j + 1]:
                L[j] = L[j + 1]
            else:
                L[j] = value
                value = L[j+1]

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

# ******************* Selection sort code VARIATION 2 *******************
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

# def selection_sort2(L):
#     for i in range(len(L) // 2):
#         min_index, max_index = find_min_max_indices(L, i, len(L) - i - 1)
#         swap(L, i, min_index)

#         if max_index == i:
#             max_index = min_index
#         swap(L, len(L) - i - 1, max_index)

# def find_min_max_indices(L, start, end):
#     min_index = start
#     max_index = start
    
#     for i in range(start, end + 1):
#         if L[i] < L[min_index]:
#             min_index = i
#         elif L[i] > L[max_index]:
#             max_index = i
            
#     return min_index, max_index


def experiment1(numberOfRuns, numberOfElements):
    total1 = 0
    total2 = 0
    total3 = 0
    for i in range(numberOfRuns):
        randomList = create_random_list(numberOfElements, 10000)

        start = timeit.default_timer()
        bubble_sort(randomList)
        total1 += timeit.default_timer() - start

        start = timeit.default_timer()
        selection_sort(randomList)
        total2 += timeit.default_timer() - start

        start = timeit.default_timer()
        insertion_sort(randomList)
        total3 += timeit.default_timer() - start
    
    x1=total1/numberOfRuns
    x2= total2/numberOfRuns
    x3= total3/numberOfRuns
    
    print("Bubble sort -- listLength: ", numberOfElements, " time: ", x1, "sec")
    print("Selection sort -- listLength: ", numberOfElements, " time: ", x2, "sec")
    print("Insertion sort -- listLength: ", numberOfElements, " time: ", x3, "sec")
    print("================================================================")
    return x1,x2,x3

def run_experiment1():

    b1,s1,i1 = experiment1(100,10)
    b2,s2,i2 = experiment1(100,100)
    b3,s3,i3 = experiment1(100,1000)
    b4,s4,i4 = experiment1(100,5000)
    b5,s5,i5 = experiment1(100,10000)

    b=[b1,b2,b3,b4,b5]
    s=[s1,s2,s3,s4,s5]
    i=[i1,i2,i3,i4,i5]
    y=[10,100,1000,5000,10000]

    fig, ax = plt.subplots()
    ax.scatter(b, y)
    ax.scatter(s, y, color='r')
    ax.scatter(i, y, color='g')

    plt.plot(b, y, label = "bubble sort")
    plt.plot(s, y, label = "selection sort")
    plt.plot(i, y, label = "insertion sort")

    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Length of List')
    ax.legend()
    ax.set_title('List length vs Time Displaying for ten runs')

    # experiment1(10,10)
    # experiment1(10,100)
    # experiment1(10,1000)
    # experiment1(10,5000)
    # experiment1(10,10000)

    # experiment1(100,10)
    # experiment1(100,100)
    # experiment1(100,1000)
    # experiment1(100,5000)
    # experiment1(100,10000)

    plt.show()


def experiment2(numberOfRuns, numberOfElements):
    total1 = 0
    total2 = 0
    total3 = 0

    total1_variation = 0
    total2_variation = 0
    total3_variation = 0
    for i in range(numberOfRuns):
        randomList = create_random_list(numberOfElements, 10000)

        start = timeit.default_timer()
        bubble_sort(randomList)
        total1 += timeit.default_timer() - start

        start = timeit.default_timer()
        selection_sort(randomList)
        total2 += timeit.default_timer() - start

        start = timeit.default_timer()
        insertion_sort(randomList)
        total3 += timeit.default_timer() - start


        start = timeit.default_timer()
        bubble_sort2(randomList)
        total1_variation += timeit.default_timer() - start

        start = timeit.default_timer()
        selection_sort2(randomList)
        total2_variation += timeit.default_timer() - start

        start = timeit.default_timer()
        insertion_sort2(randomList)
        total3_variation += timeit.default_timer() - start
    
    x1=total1/numberOfRuns
    x2= total2/numberOfRuns
    x3= total3/numberOfRuns

    x1_variation =total1_variation/numberOfRuns
    x2_variation = total2_variation/numberOfRuns
    x3_variation = total3_variation/numberOfRuns
    
    print("Bubble sort -- listLength: ", numberOfElements, " time: ", x1, "sec")
    print("Selection sort -- listLength: ", numberOfElements, " time: ", x2, "sec")
    print("Insertion sort -- listLength: ", numberOfElements, " time: ", x3, "sec")
    print("------------------------------------------------------------------")
    print("Bubble sort variation-- listLength: ", numberOfElements, " time: ", x1_variation, "sec")
    print("Selection sort variation -- listLength: ", numberOfElements, " time: ", x2_variation, "sec")
    print("Insertion sort variation -- listLength: ", numberOfElements, " time: ", x3_variation, "sec")
    print("================================================================")
    return x1,x2,x3, x1_variation, x2_variation, x3_variation

def main():

    L = [7, 2, 5, 9, 1, 4, 3, 6,8,10,9]
    print(bubble_sort2(L))
    #selection_sort2(L)

    print("final   ", L)

main()