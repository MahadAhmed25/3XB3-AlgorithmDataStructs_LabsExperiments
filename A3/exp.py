import time
from knapsack import *
import matplotlib.pyplot as plt


def graph_and_run_experimentTDBT(maxval_weight, capacity):
    num_itemsBot=[]
    run_timeBot =[]

    counter =0
    for current_items in range(10, 110, 10):
        sack = create_knapsack(current_items, 1, maxval_weight, 1, maxval_weight)
        start=0; end=0
        start = time.time()
        result = ks_bottom_up(sack, capacity)
        end = time.time()
        num_itemsBot.append(current_items)
        run_timeBot.append(end-start)
        counter+=1

    
    num_itemsTop=[]
    run_timeTop =[]

    counter2=0
    for current_items in range(10, 110, 10):
        sack = create_knapsack(current_items, 1, maxval_weight, 1, maxval_weight)
        start=0; end=0
        start = time.time()
        result = ks_top_down(sack, capacity)
        end = time.time()
        num_itemsTop.append(current_items)
        run_timeTop.append(end-start)
        counter2+=1

    plt.plot(num_itemsBot, run_timeBot,color='r')
    plt.plot(num_itemsTop, run_timeTop, color='g')

    plt.legend(["Bottom Up", "Top Down"], loc ="lower right")
    plt.xlabel('Number of items in knapsack')
    plt.ylabel('Time in seconds')
    plt.title('Runtime vs Number of Items')
    plt.show()



#graph_and_run_experimentRBF(10,10)
graph_and_run_experimentTDBT(300,80)