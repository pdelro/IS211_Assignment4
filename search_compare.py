import argparse
# other imports go here

import random
import time

def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list
    
def sequential_search(a_list,item):
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found


def ordered_sequential_search(a_list,item):
    return sorted(a_list)
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1
    return found


def binary_search_iterative(a_list,item):
    return sorted(a_list)
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found

    
def binary_search_recursive(a_list,item):
    return sorted(a_list)
    if len(a_list) == 0:
        found = False
    else:
        midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
        found = True
    else:
        if item < a_list[midpoint]:
            return binary_search_recursive(a_list[:midpoint], item)
        else:
            return binary_search_recursive(a_list[midpoint + 1], item)


def main():
    random.seed(100)

    list_sizes = [500, 1000, 5000]
    total_time = 0

    for list_size in list_sizes:
        for i in range(100):
            myList = get_me_random_list(list_size)
            start = time.time()
            sequential_search(myList, 99999999)
            end = time.time()
            sort_time = end - start
            total_time += sort_time

        avg_time = total_time / 100
        print(type(avg_time))
        print(f"Sequential Search with list size of {list_size} took%10.7f seconds to run, on average" % (avg_time))

    for list_size in list_sizes:
        for i in range(100):
            myList = get_me_random_list(list_size)
            start = time.time()
            ordered_sequential_search(myList, 99999999)
            end = time.time()
            sort_time = end - start
            total_time += sort_time

        avg_time = total_time / 100
        print(f"Ordered Sequential Search with list size of {list_size} took%10.7f seconds to run, on average" % (avg_time))

    for list_size in list_sizes:
        for i in range(100):
            myList = get_me_random_list(list_size)
            start = time.time()
            binary_search_iterative(myList, 99999999)
            end = time.time()
            sort_time = end - start
            total_time += sort_time

        avg_time = total_time / 100
        print(f"Iterative Binary Search with list size of {list_size} took%10.7f seconds to run, on average" % (avg_time))

    for list_size in list_sizes:
        for i in range(100):
            myList = get_me_random_list(list_size)
            start = time.time()
            binary_search_recursive(myList, 99999999)
            end = time.time()
            sort_time = end - start
            total_time += sort_time

        avg_time = total_time / 100
        print(f"Recursive Binary Search with list size of {list_size} took%10.7f seconds to run, on average" % (avg_time))


if __name__ == "__main__":
    """Main entry point"""
    main()