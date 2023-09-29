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
    value = L[i]
    while i > 0:
        if L[i - 1] > value:
            L[i] = L[i - 1]
            i -= 1
        else:
            L[i] = value
            return
    L[0] = value 



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
        L[len(L)-1] = value

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



# ******************* Experiment 1 *******************
def experiment1(numberOfRuns, numberOfElements):
    total1 = 0
    total2 = 0
    total3 = 0
    maxValue = 10000
    for _ in range(numberOfRuns):
        randomList = create_random_list(numberOfElements, maxValue)


        start = timeit.default_timer()
        selection_sort(randomList)
        total2 += timeit.default_timer() - start

        start = timeit.default_timer()
        bubble_sort(randomList)
        total1 += timeit.default_timer() - start

        start = timeit.default_timer()
        insertion_sort(randomList)
        total3 += timeit.default_timer() - start
    
    x1=total1/numberOfRuns
    x2= total2/numberOfRuns
    x3= total3/numberOfRuns
    
    print("Bubble sort -- listLength: ", numberOfElements, "runs: ", numberOfRuns, " time: ", x1, "sec")
    print("Selection sort -- listLength: ", numberOfElements, "runs: ", numberOfRuns, " time: ", x2, "sec")
    print("Insertion sort -- listLength: ", numberOfElements, "runs: ", numberOfRuns, " time: ", x3, "sec")
    print("================================================================")
    return x1,x2,x3

def graph_and_run_experiment1():
    print("====================RESULTS for 1 Run====================")
    experiment1(1,10)
    experiment1(1,100)
    experiment1(1,1000)
    experiment1(1,3000)
    experiment1(1,5000)

    print("====================RESULTS for 10 Run====================")
    b1,s1,i1 = experiment1(10,10)
    b2,s2,i2 = experiment1(10,100)
    b3,s3,i3 = experiment1(10,1000)
    b4,s4,i4 = experiment1(10,3000)
    b5,s5,i5 = experiment1(10,5000)

    b=[b1,b2,b3,b4,b5]
    s=[s1,s2,s3,s4,s5]
    i=[i1,i2,i3,i4,i5]
    x=[10,100,1000,3000,5000]

    fig, ax = plt.subplots()
    ax.scatter(x, b)
    ax.scatter(x, s, color='r')
    ax.scatter(x, i, color='g')

    plt.plot(x, b, label = "bubble sort")
    plt.plot(x, s, label = "selection sort")
    plt.plot(x, i, label = "insertion sort")

    ax.set_ylabel('Time (seconds)')
    ax.set_xlabel('Length of List')
    ax.legend()
    ax.set_title('List length vs Time for 10 runs of all 3 bad sorts')

    plt.show()


# ******************* Experiment 2 *******************
def experiment2(numberOfRuns, numberOfElements):
    maxValue = 10000
    total_bubble = 0
    total_selection = 0
    total_insertion = 0

    total_bubble_variation = 0
    total_selection_variation = 0
    total_insertion_variation = 0

    for _ in range(numberOfRuns):
        randomList = create_random_list(numberOfElements, maxValue)

        start = timeit.default_timer()
        bubble_sort(randomList)
        total_bubble += timeit.default_timer() - start

        start = timeit.default_timer()
        bubble_sort2(randomList)
        total_bubble_variation += timeit.default_timer() - start

        start = timeit.default_timer()
        selection_sort(randomList)
        total_selection += timeit.default_timer() - start

        start = timeit.default_timer()
        selection_sort2(randomList)
        total_selection_variation += timeit.default_timer() - start

        start = timeit.default_timer()
        insertion_sort(randomList)
        total_insertion += timeit.default_timer() - start

        start = timeit.default_timer()
        insertion_sort2(randomList)
        total_insertion_variation += timeit.default_timer() - start
    
    x_bubble = total_bubble/numberOfRuns
    x_selection = total_selection/numberOfRuns
    x_insertion = total_insertion/numberOfRuns

    x_bubble_variation =total_bubble_variation/numberOfRuns
    x_selection_variation = total_selection_variation/numberOfRuns
    x_insertion_variation = total_insertion_variation/numberOfRuns
    
    print("Bubble sort -- listLength: ", numberOfElements, "runs: ", numberOfRuns, " time: ", x_bubble, "sec")
    print("Bubble sort variation-- listLength: ", numberOfElements, "runs: ", numberOfRuns, " time: ", x_bubble_variation, "sec")

    print("------------------------------------------------------------------")
    
    print("Selection sort -- listLength: ", numberOfElements, "runs: ", numberOfRuns, " time: ", x_selection, "sec")
    print("Selection sort variation -- listLength: ", numberOfElements, "runs: ", numberOfRuns, " time: ", x_selection_variation, "sec")
    
    print("------------------------------------------------------------------")

    print("Insertion sort -- listLength: ", numberOfElements, "runs: ", numberOfRuns, " time: ", x_insertion, "sec")
    print("Insertion sort variation -- listLength: ", numberOfElements, "runs: ", numberOfRuns, " time: ", x_insertion_variation, "sec")
    print("================================================================")

    return x_bubble, x_selection, x_insertion, x_bubble_variation, x_selection_variation, x_insertion_variation


def graph_and_run_experiment2():
    print("====================RESULTS for 1 Run====================")
    experiment2(1,10)
    experiment2(1,100)
    experiment2(1,1000)
    experiment2(1,3000)
    experiment2(1,5000)
    
    print("====================RESULTS for 10 Runs====================")
    b1,s1,i1,bv1,sv1,iv1 = experiment2(10,10)
    b2,s2,i2,bv2,sv2,iv2 = experiment2(10,100)
    b3,s3,i3,bv3,sv3,iv3 = experiment2(10,1000)
    b4,s4,i4,bv4,sv4,iv4 = experiment2(10,3000)
    b5,s5,i5,bv5,sv5,iv5 = experiment2(10,5000)
    
    y = [10, 100, 1000, 3000, 5000]

    # Data for the sorts
    bubble_data = [b1, b2, b3, b4, b5]
    bubble_variation_data = [bv1, bv2, bv3, bv4, bv5]
    selection_data = [s1, s2, s3, s4, s5]
    selection_variation_data = [sv1, sv2, sv3, sv4, sv5]
    insertion_data = [i1, i2, i3, i4, i5]
    insertion_variation_data = [iv1, iv2, iv3, iv4, iv5]

    # plot bubble sort vs variation
    fig, ax = plt.subplots()
    ax.scatter(y, bubble_data, color='r')
    ax.scatter(y, bubble_variation_data, color='b')
    ax.plot(y, bubble_data, color='r', label='Bubble sort')
    ax.plot(y, bubble_variation_data, color='b', label='Bubble sort variation')
    ax.set_xlabel('Length of List')
    ax.set_ylabel('Time (seconds)')
    ax.legend()
    ax.set_title('List Length vs Time for 10 runs comparing Bubble Sort vs Bubble Sort Variation')
    plt.show()

    # plot selection sort vs variation
    fig, ax = plt.subplots()
    ax.scatter(y, selection_data, color='r')
    ax.scatter(y, selection_variation_data, color='b')
    ax.plot(y, selection_data, color='r', label='Selection sort')
    ax.plot(y, selection_variation_data, color='b', label='Selection sort variation')
    ax.set_xlabel('Length of List')
    ax.set_ylabel('Time (seconds)')
    ax.legend()
    ax.set_title('List Length vs Time for 10 runs comparing Selection Sort vs Selection Sort Variation')
    plt.show()

    # plot insertion sort vs variation
    fig, ax = plt.subplots()
    ax.scatter(y, insertion_data, color='r')
    ax.scatter(y, insertion_variation_data, color='b')
    ax.plot(y, insertion_data, color='r', label='Insertion sort')
    ax.plot(y, insertion_variation_data, color='b', label='Insertion sort variation')
    ax.set_xlabel('Length of List')
    ax.set_ylabel('Time (seconds)')
    ax.legend()
    ax.set_title('List Length vs Time for 10 runs comparing Insertion Sort vs Insertion Sort Variation')
    plt.show()

    

# ******************* Experiment 3 *******************
def experiment3(numberOfRuns, maxSwaps, listLength=10000):
    maxValue = 10000
    
    total1, total2, total3 = 0, 0, 0

    for i in range(numberOfRuns):
        nearSortedlist = create_near_sorted_list(listLength, maxValue, maxSwaps)

        start = timeit.default_timer()
        bubble_sort(nearSortedlist)
        total1 += timeit.default_timer() - start

        start = timeit.default_timer()
        selection_sort(nearSortedlist)
        total2 += timeit.default_timer() - start

        start = timeit.default_timer()
        insertion_sort(nearSortedlist)
        total3 += timeit.default_timer() - start

    x1=total1/numberOfRuns
    x2= total2/numberOfRuns
    x3= total3/numberOfRuns

    print("==============Results for sorting near sorted list===============")
    print("Bubble sort -- swaps: ", maxSwaps, "runs: ", numberOfRuns, " time: ", x1, "sec")
    print("Selection sort -- swaps: ", maxSwaps, "runs: ", numberOfRuns, " time: ", x2, "sec")
    print("Insertion sort -- swaps: ", maxSwaps, "runs: ", numberOfRuns, " time: ", x3, "sec")
    print("=================================================================")

    return x1, x2, x3



def graph_and_run_experiment3(): 
    print("====================RESULTS for 1 Run====================")
    experiment3(1,10)
    experiment3(1,100)
    experiment3(1,1000)
    experiment3(1,3000)
    experiment3(1,5000)
    
    print("====================RESULTS for 10 Runs====================")
    b1,s1,i1 = experiment3(10,10)
    b2,s2,i2 = experiment3(10,100)
    b3,s3,i3 = experiment3(10,1000)
    b4,s4,i4 = experiment3(10,3000)
    b5,s5,i5 = experiment3(10,5000)

    b=[b1,b2,b3,b4,b5]
    s=[s1,s2,s3,s4,s5]
    i=[i1,i2,i3,i4,i5]
    x=[10,100,1000,3000,5000]

    fig, ax = plt.subplots()
    plt.plot(x, b, label = "bubble sort")
    plt.plot(x, s, label = "selection sort")
    plt.plot(x, i, label = "insertion sort")

    ax.set_xlabel('swaps')
    ax.set_ylabel('time')
    ax.legend()
    ax.set_title('Number of Swaps vs Time for 10 runs comparing all 3 bad sorts')
    
    plt.show()



def main():
    L=[1,3,23,21,56,5,69,32,2,4,8]
    a=bubble_sort2(L)
    print(a)
    #graph_and_run_experiment1()
    #graph_and_run_experiment2()
    #graph_and_run_experiment3()
main()