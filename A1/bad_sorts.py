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
        
# ******************* Insertion sort code VARIATION 1 *******************

def insertion_sort2(L):
    for i in range(1, len(L)):
        print(L)
        insert2(L, i)

def insert2(L, i):
    current_element = L[i]
    j = i - 1

    while j >= 0 and L[j] > current_element:
        L[j + 1] = L[j]
        j -= 1

    L[j + 1] = current_element



# ******************* Bubble sort code *******************

# Traditional Bubble sort
def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                swap(L, j, j+1)


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

def experiment(numberOfRuns, numberOfElements):
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

    b1,s1,i1 = experiment(100,10)
    b2,s2,i2 = experiment(100,100)
    b3,s3,i3 = experiment(100,1000)
    b4,s4,i4 = experiment(100,5000)
    b5,s5,i5 = experiment(100,10000)

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

    # experiment(10,10)
    # experiment(10,100)
    # experiment(10,1000)
    # experiment(10,5000)
    # experiment(10,10000)

    # experiment(100,10)
    # experiment(100,100)
    # experiment(100,1000)
    # experiment(100,5000)
    # experiment(100,10000)

    plt.show()

def main():

    L = [7, 2, 5, 9, 1, 4, 3, 6, 8]
    insertion_sort2(L)

main()