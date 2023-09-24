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
    
    print("Bubble sort -- listLength: ", numberOfElements, " time: ", x_bubble, "sec")
    print("Bubble sort variation-- listLength: ", numberOfElements, " time: ", x_bubble_variation, "sec")

    print("------------------------------------------------------------------")
    
    print("Selection sort -- listLength: ", numberOfElements, " time: ", x_selection, "sec")
    print("Selection sort variation -- listLength: ", numberOfElements, " time: ", x_selection_variation, "sec")
    
    print("------------------------------------------------------------------")

    print("Insertion sort -- listLength: ", numberOfElements, " time: ", x_insertion, "sec")
    print("Insertion sort variation -- listLength: ", numberOfElements, " time: ", x_insertion_variation, "sec")
    print("================================================================")
    
    # return x_bubble, x_bubble_variation

    return x_bubble, x_selection, x_insertion, x_bubble_variation, x_selection_variation, x_insertion_variation

def run_experiment2():

    b1,s1,i1, b_variation1, s_variation1, i_variation1  = experiment2(1,10)
    b2,s2,i2, b_variation2, s_variation2, i_variation2 = experiment2(1,100)
    b3,s3,i3, b_variation3, s_variation3, i_variation3 = experiment2(1,1000)
    b4,s4,i4, b_variation4, s_variation4, i_variation4 = experiment2(1,5000)
    b5,s5,i5, b_variation5, s_variation5, i_variation5 = experiment2(1,10000)

    b=[b1,b2,b3,b4,b5]
    b_variation = [b_variation1, b_variation2, b_variation3, b_variation4, b_variation5]
    s=[s1,s2,s3,s4,s5]
    s_variation=[s_variation1, s_variation2, s_variation3, s_variation4, s_variation5]
    i=[i1,i2,i3,i4,i5]
    i_variation=[i_variation1, i_variation2, i_variation3, i_variation4, i_variation5]
    
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

    print("====================================RESULTS============================")
    
    experiment2(10,10)
    experiment2(10,100)
    experiment2(10,1000)
    experiment2(10,5000)
    experiment2(10,10000)

# ******************* Experiment 3 *******************
# def experiment3(numberOfRuns, swaps, list_length=1000, max_value=10000):
#     total1=0
#     total2=0
#     total3=0

#     for _ in range(numberOfRuns):
#         near_sorted_list = create_near_sorted_list(list_length, max_value, swaps)
#         start = timeit.default_timer()
#         bubble_sort(near_sorted_list.copy())  # Create a copy to ensure the same list is used for all algorithms
#         total1 += timeit.default_timer() - start

#         start = timeit.default_timer()
#         selection_sort(near_sorted_list.copy())
#         total2 += timeit.default_timer() - start

#         start = timeit.default_timer()
#         insertion_sort(near_sorted_list.copy())
#         total3 += timeit.default_timer() - start

#     avg_time_bubble = total1 / numberOfRuns
#     avg_time_selection = total2 / numberOfRuns
#     avg_time_insertion = total3 / numberOfRuns

#     print("Bubble sort -- List Length:", list_length, "Swaps:", swaps, "Average Time:", avg_time_bubble, "sec")
#     print("Selection sort -- List Length:", list_length, "Swaps:", swaps, "Average Time:", avg_time_selection, "sec")
#     print("Insertion sort -- List Length:", list_length, "Swaps:", swaps, "Average Time:", avg_time_insertion, "sec")
#     print("================================================================")

#     return avg_time_bubble, avg_time_selection, avg_time_insertion

# def run_experiment3():
#     avg_time_bubble, avg_time_selection, avg_time_insertion = experiment3(1, 10)
#     avg_time_bubble, avg_time_selection, avg_time_insertion = experiment3(1, 100)
#     avg_time_bubble, avg_time_selection, avg_time_insertion = experiment3(1, 500)
#     avg_time_bubble, avg_time_selection, avg_time_insertion = experiment3(1, 1000)

#     avg_time_bubble, avg_time_selection, avg_time_insertion = experiment3(10, 10)
#     avg_time_bubble, avg_time_selection, avg_time_insertion = experiment3(10, 100)
#     avg_time_bubble, avg_time_selection, avg_time_insertion = experiment3(10, 500)
#     avg_time_bubble, avg_time_selection, avg_time_insertion = experiment3(10, 1000)


def experiment3(numberOfRuns, maxSwaps, listLength=1000):
    total_times_bubble = []
    total_times_selection = []
    total_times_insertion = []
    swap_values = list(range(0, maxSwaps + 1))

    for swaps in swap_values:
        total1 = 0
        total2 = 0
        total3 = 0

        for _ in range(numberOfRuns):
            near_sorted_list = create_near_sorted_list(listLength, maxSwaps, swaps)

            start = timeit.default_timer()
            bubble_sort(near_sorted_list.copy())  # Create a copy to ensure the same list is used for all algorithms
            total1 += timeit.default_timer() - start

            start = timeit.default_timer()
            selection_sort(near_sorted_list.copy())
            total2 += timeit.default_timer() - start

            start = timeit.default_timer()
            insertion_sort(near_sorted_list.copy())
            total3 += timeit.default_timer() - start

        avg_time_bubble = total1 / numberOfRuns
        avg_time_selection = total2 / numberOfRuns
        avg_time_insertion = total3 / numberOfRuns

        total_times_bubble.append(avg_time_bubble)
        total_times_selection.append(avg_time_selection)
        total_times_insertion.append(avg_time_insertion)

    plt.figure(figsize=(10, 6))
    plt.plot(swap_values, total_times_bubble, label='Bubble Sort')
    plt.plot(swap_values, total_times_selection, label='Selection Sort')
    plt.plot(swap_values, total_times_insertion, label='Insertion Sort')
    plt.xlabel('Number of Random Swaps')
    plt.ylabel('Average Time (seconds)')
    plt.title(f'Swaps vs Time for List Length {listLength}')
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    experiment3(1, 500)

main()