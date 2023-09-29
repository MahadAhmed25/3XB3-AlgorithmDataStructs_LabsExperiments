"""
This file corresponds to the first graded lab of 2XC3.
Feel free to modify and/or add functions to this file.

In contains traditional implementations for:
1) Quick sort
2) Merge sort
3) Heap sort

Author: Vincent Maccio
"""
import math
import timeit
import matplotlib.pyplot as plt
import numpy as np
import random
from bad_sorts import insertion_sort

def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]

# ************ Quick Sort ************
def quicksort(L):
    copy = quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def quicksort_copy(L):
    if len(L) < 2:
        return L
    pivot = L[0]
    left, right = [], []
    for num in L[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    return quicksort_copy(left) + [pivot] + quicksort_copy(right)


# ************ Dual Pivot Quick Sort ************
def dual_quicksort(L):
    if len(L) < 2:
        return L
    pivot1, pivot2 = L[0], L[1]
    left, right, middle = [], [], []

    if pivot1 > pivot2:
        t = pivot1
        pivot1 = pivot2
        pivot2 = t

    for num in L[2:]:
        if num < pivot1:
            left.append(num)
        elif num > pivot2:
            right.append(num)
        else:
            middle.append(num)

    return dual_quicksort(left) + [pivot1] + dual_quicksort(middle) + [pivot2] + dual_quicksort(right)


# ************ Merge Sort *************

def mergesort(L):
    if len(L) <= 1:
        return
    mid = len(L) // 2
    left, right = L[:mid], L[mid:]

    mergesort(left)
    mergesort(right)
    temp = merge(left, right)

    for i in range(len(temp)):
        L[i] = temp[i]


def merge(left, right):
    L = []
    i = j = 0

    while i < len(left) or j < len(right):
        if i >= len(left):
            L.append(right[j])
            j += 1
        elif j >= len(right):
            L.append(left[i])
            i += 1
        else:
            if left[i] <= right[j]:
                L.append(left[i])
                i += 1
            else:
                L.append(right[j])
                j += 1
    return L

def bottom_up_mergesort(a):
    width = 1   
    n = len(a)                           
    while (width < n):
        l=0
        while (l < n):
            r = min(l+(width*2-1), n-1)        
            m = min(l+width-1,n-1)          
            merge2(a, l, m, r)
            l += width*2
        width *= 2
    return a
   
def merge2(a, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = a[l + i]
    for i in range(0, n2):
        R[i] = a[m + i + 1]
 
    i, j, k = 0, 0, l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
        k += 1
 
    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1
 
    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1

# *************************************

# ************* Heap Sort *************

def heapsort(L):
    heap = Heap(L)
    for _ in range(len(L)):
        heap.extract_max()

class Heap:
    length = 0
    data = []

    def __init__(self, L):
        self.data = L
        self.length = len(L)
        self.build_heap()

    def build_heap(self):
        for i in range(self.length // 2 - 1, -1, -1):
            self.heapify(i)

    def heapify(self, i):
        largest_known = i
        if self.left(i) < self.length and self.data[self.left(i)] > self.data[i]:
            largest_known = self.left(i)
        if self.right(i) < self.length and self.data[self.right(i)] > self.data[largest_known]:
            largest_known = self.right(i)
        if largest_known != i:
            self.data[i], self.data[largest_known] = self.data[largest_known], self.data[i]
            self.heapify(largest_known)

    def insert(self, value):
        if len(self.data) == self.length:
            self.data.append(value)
        else:
            self.data[self.length] = value
        self.length += 1
        self.bubble_up(self.length - 1)

    def insert_values(self, L):
        for num in L:
            self.insert(num)

    def bubble_up(self, i):
        while i > 0 and self.data[i] > self.data[self.parent(i)]:
            self.data[i], self.data[self.parent(i)] = self.data[self.parent(i)], self.data[i]
            i = self.parent(i)

    def extract_max(self):
        self.data[0], self.data[self.length - 1] = self.data[self.length - 1], self.data[0]
        max_value = self.data[self.length - 1]
        self.length -= 1
        self.heapify(0)
        return max_value

    def left(self, i):
        return 2 * (i + 1) - 1

    def right(self, i):
        return 2 * (i + 1)

    def parent(self, i):
        return (i + 1) // 2 - 1

    def __str__(self):
        height = math.ceil(math.log(self.length + 1, 2))
        whitespace = 2 ** height
        s = ""
        for i in range(height):
            for j in range(2 ** i - 1, min(2 ** (i + 1) - 1, self.length)):
                s += " " * whitespace
                s += str(self.data[j]) + " "
            s += "\n"
            whitespace = whitespace // 2
        return s

# *************************************
#Expieremnt 4 

def experiment4(numberOfRuns, numberOfElements):
    total1 = 0
    total2 = 0
    total3 = 0
    for i in range(numberOfRuns):
        randomList = create_random_list(numberOfElements, 10000)

        start = timeit.default_timer()
        quicksort(randomList)
        total1 += timeit.default_timer() - start

        start = timeit.default_timer()
        mergesort(randomList)
        total2 += timeit.default_timer() - start

        start = timeit.default_timer()
        heapsort(randomList)
        total3 += timeit.default_timer() - start
    
    x1=total1/numberOfRuns
    x2= total2/numberOfRuns
    x3= total3/numberOfRuns
    
    print("Quick sort -- listLength: ", numberOfElements, " time: ", x1, "sec")
    print("Merge sort -- listLength: ", numberOfElements, " time: ", x2, "sec")
    print("Heap sort -- listLength: ", numberOfElements, " time: ", x3, "sec")
    print("================================================================")
    return x1,x2,x3

def run_experiment_4():
    q1,m1,h1 = experiment4(10,10)
    q2,m2,h2 = experiment4(10,100)
    q3,m3,h3 = experiment4(10,1000)
    q4,m4,h4 = experiment4(10,3000)
    q5,m5,h5 = experiment4(10,5000)

    q=[q1,q2,q3,q4,q5]
    m=[m1,m2,m3,m4,m5]
    h=[h1,h2,h3,h4,h5]
    x=[10,100,1000,3000,5000]

    fig, ax = plt.subplots()

    plt.plot(x, q, label = "Quick sort")
    plt.plot(x, m, label = "Merge sort")
    plt.plot(x, h, label = "Heap sort")

    ax.set_xlabel('Length of List')
    ax.set_ylabel('Time (seconds)')
    ax.legend()
    ax.set_title('List length vs Time Displaying for 10 runs of "Good Sort"')


    plt.show()

# *************************************
#Expieremnt 5

def create_near_sorted_list(length, max_value, swaps):
    L = create_random_list(length, max_value)
    L.sort()
    for _ in range(swaps):
        r1 = random.randint(0, length - 1)
        r2 = random.randint(0, length - 1)
        swap(L, r1, r2)
    return L

def swap(L, i, j):
    L[i], L[j] = L[j], L[i] 

def experiment5(numberOfRuns,numberOfElements,swaps):
    total1 = 0
    total2 = 0
    total3 = 0
    max_value= 10000

    for i in range(numberOfRuns):
        swapped_list= create_near_sorted_list(numberOfElements,max_value,swaps)
        start = timeit.default_timer()
        quicksort(swapped_list)
        total1 += timeit.default_timer() - start

        start = timeit.default_timer()
        mergesort(swapped_list)
        total2 += timeit.default_timer() - start

        start = timeit.default_timer()
        heapsort(swapped_list)
        total3 += timeit.default_timer() - start
    
    x1=total1/numberOfRuns
    x2= total2/numberOfRuns
    x3= total3/numberOfRuns
    
    print("Quick sort -- listLength: ", numberOfElements, " time: ", x1, "sec")
    print("Merge sort -- listLength: ", numberOfElements, " time: ", x2, "sec")
    print("Heap sort -- listLength: ", numberOfElements, " time: ", x3, "sec")
    print("================================================================")
    return x1,x2,x3

def run_experiment_5():

    q1,m1,h1 = experiment5(1,1000,1)
    q2,m2,h2 = experiment5(1,1000,10)
    q3,m3,h3 = experiment5(1,1000,100)
    q4,m4,h4 = experiment5(1,1000,200)
    q5,m5,h5 = experiment5(1,1000,300)
    q6,m6,h6 = experiment5(1,1000,400)
    q7,m7,h7 = experiment5(1,1000,500)
    #q8,m8,h8 = experiment5(1,1000,600)
    #q9,m9,h9 = experiment5(1,1000,700)

    q=[q1,q2,q3,q4,q5,q6,q7]#,q8,q9]
    m=[m1,m2,m3,m4,m5,m6,m7]#,m8,m9]
    h=[h1,h2,h3,h4,h5,h6,h7]#,h8,h9]
    y=[1,10,100,200,300,400,500]#,600,700]

    fig, ax = plt.subplots()

    plt.plot(y, q, label = "Quick sort")
    plt.plot(y, m, label = "Merge sort")
    plt.plot(y, h, label = "Heap sort")

    ax.set_xlabel('Swaps')
    ax.set_ylabel('Time (seconds)')
    ax.legend()
    ax.set_title('Swap vs Time for 10 runs')



    plt.show()

    

def experiment6(numberOfRuns, listLength = 10000):
    maxValue = 10000
    total1, total2  = 0, 0

    for _ in range(numberOfRuns):
        randomList = create_random_list(listLength, maxValue)

        start = timeit.default_timer()
        mergesort(list)
        total1 += timeit.default_timer() - start

        start = timeit.default_timer()
        bottom_up_mergesort(list)
        total2 += timeit.default_timer() - start

    x1=total1/numberOfRuns
    x2= total2/numberOfRuns

    print("==============Results for sorting near sorted list===============")
    print("Merge Sort -- legnth: ", listLen, " time: ", x1, "sec")
    print("Iterative Merge sort -- legnth: ", listLen, " time: ", x2, "sec")
    print("=================================================================")

    return x1, x2


def graph_and_run_experiment6():
    b1,bt1 = experiment6(10,10)
    b1,bt1 = experiment6(10,100)
    b2,bt2 = experiment6(10,1000)
    b3,bt3 = experiment6(10,3000)
    b4,bt4 = experiment6(10,5000)

    b1=[b11,b12,b13,b14,b15,b16]
    b2=[b21,b22,b23,b24]
    x=[10,100,1000,3000,5000]

    fig, ax = plt.subplots()
    ax.scatter(x, b1)
    ax.scatter(x, b2)

    plt.plot(x, b1, label = "traditional quick sort")
    plt.plot(x, b2, label = "dual pivot quick sort")

    ax.set_ylabel('Time (seconds)')
    ax.set_xlabel('Length of List')
    ax.legend()
    ax.set_title('List length vs Time Comparing Merge sort vs Iterative Merge Sort for 10 Runs')

    plt.show()


def experiment7(numberOfRuns, listLen = 1000):
    maxValue = 10000
    
    total1, total2  = 0, 0

    for i in range(numberOfRuns):
        list = create_random_list(listLen, maxValue)

        start = timeit.default_timer()
        mergesort(list)
        total1 += timeit.default_timer() - start

        start = timeit.default_timer()
        bottom_up_mergesort(list)
        total2 += timeit.default_timer() - start

    x1=total1/numberOfRuns
    x2= total2/numberOfRuns

    print("==============Results for sorting near sorted list===============")
    print("Merge Sort -- legnth: ", listLen, " time: ", x1, "sec")
    print("Iterative Merge sort -- legnth: ", listLen, " time: ", x2, "sec")
    print("=================================================================")

    return x1, x2

def graphExperiment7():
    b11,b21 = experiment7(10,10)
    b12,b22 = experiment7(10,1000)
    b13,b23 = experiment7(10,3000)
    b14,b24 = experiment7(10,5000)
    b15,b25 = experiment7(10,8000)
    b16,b26 = experiment7(10,10000)

    b1=[b11,b12,b13,b14,b15,b16]
    b2=[b21,b22,b23,b24,b25,b26]
    x=[10,100,500,1000,5000,10000]

    fig, ax = plt.subplots()
    ax.scatter(x, b1)
    ax.scatter(x, b2)

    plt.plot(x, b1, label = "traditional merge sort")
    plt.plot(x, b2, label = "iterative merge sort")

    ax.set_ylabel('Time (seconds)')
    ax.set_xlabel('Length of List')
    ax.legend()
    ax.set_title('List length vs Time Comparing Merge sort vs Iterative Merge Sort for 10 Runs')

    plt.show()

def experiment8(numberOfRuns, numberOfElements):
    total1 = 0
    total2 = 0
    total3 = 0
    for i in range(numberOfRuns):
        randomList = create_random_list(numberOfElements, 100)

        start = timeit.default_timer()
        insertion_sort(randomList)
        total1 += timeit.default_timer() - start

        start = timeit.default_timer()
        mergesort(randomList)
        total2 += timeit.default_timer() - start

        start = timeit.default_timer()
        quicksort(randomList)
        total3 += timeit.default_timer() - start
    
    x1=total1/numberOfRuns
    x2= total2/numberOfRuns
    x3= total3/numberOfRuns
    
    print("Insertion sort -- listLength: ", numberOfElements, " time: ", x1, "sec")
    print("Merge sort -- listLength: ", numberOfElements, " time: ", x2, "sec")
    print("quick sort -- listLength: ", numberOfElements, " time: ", x3, "sec")
    print("================================================================")
    return x1,x2,x3


def graphExperiment8():

    i1,m1,q1 = experiment8(100,3)
    i2,m2,q2 = experiment8(100,7)
    i3,m3,q3 = experiment8(100,11)
    i4,m4,q4 = experiment8(100,15)
    i5,m5,q5 = experiment8(100,20)

    i=[i1,i2,i3,i4,i5]
    m=[m1,m2,m3,m4,m5]
    q=[q1,q2,q3,q4,q5]
    y=[3,7,11,15,20]

    fig, ax = plt.subplots()
    ax.scatter(i, y)
    ax.scatter(m, y, color='r')
    ax.scatter(q, y, color='g')

    plt.plot(i, y, label = "Insertion sort")
    plt.plot(m, y, label = "Merge sort")
    plt.plot(q, y, label = "Quick sort")

    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Length of List')
    ax.legend()
    ax.set_title('List length vs Time Displaying for 100 runs of "Good Sort vs Bad Sort"')


    plt.show()


def main():
    #graphExperiment8()
    run_experiment_5()

main()