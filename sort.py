# Sort Algorithms Alphabetically
# Bubble Sort Algorithm
def bubble(array):
    for j in array:
        for i in range(0, len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
    return array

# Selection Sort
def selection(array):
    count = 0
    innerloop = 0
    min_num = 1000000000
    min_pos = 0
    for element in array: # Loop through array
        for j in range(innerloop, len(array)): # Decreases array search space
            if array[j] < min_num:
                min_num = array[j]
                min_pos = count
            count += 1
        array[innerloop], array[min_pos] = array[min_pos], array[innerloop]
        innerloop += 1
        min_num = 1000000000
        count = innerloop
    return array


# Insertion Sort
def insertion(array):
    sorted_to = 0
    found = False
    for sorted_to in range(0, len(array)-1): # Checking not out of bounds
        next_element = array[sorted_to+1]
        for element in range(sorted_to, -1, -1):
            if array[element] > next_element:
                found = True
                found_pos = element
        if found: # If there is a number lower
            temp = next_element
            for new_elem in range(sorted_to+1, found_pos, -1):
                array[new_elem] = array[new_elem-1]
            array[found_pos] = temp
        found = False
    return array


# Quick Sort Pivot Algorithm - https://www.tutorialspoint.com/data_structures_algorithms/quick_sort_algorithm.htm
def quick(array):
    print("quick sort not yet implemented")


# Merge Sort Algorithm
def merge(array):
    print("merge sort not yet implemented")


# Heap Sort Algorithm
def heap(array):
    print("heap sort not yet implemented")


# Radix Sort Algorithm
def radix(array):
    print("radix sort not yet implemented")


# Tree Sort Algorithm
def tree(array):
    print("tree sort not yet implemented")


# Counting Sort Algorithm
def counting(array):
    print("counting sort not yet implemented")


# Bucket Sort Algorithm
def bucket(array):
    print("bucket sort not yet implemented")
