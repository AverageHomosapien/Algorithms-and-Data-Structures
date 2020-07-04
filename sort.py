
# Selection Sort
def selection(array):
    count = 0
    innerloop = 0
    min_num = 10000000
    min_pos = 0
    for element in array: # Loop through array
        for j in range(innerloop, len(array)): # Decreases array search space
            if array[j] < min_num:
                min_num = array[j]
                min_pos = count
            count += 1
        array[innerloop], array[min_pos] = array[min_pos], array[innerloop]
        innerloop += 1
        min_num = 10000000
        count = innerloop
    return array

# Insertion Sort
def insertion(array):
    sorted_to = 1
    while sorted_to < len(array):
        next_element = array[sorted_to+1]
        for element in range(0, sorted_to):
            if element < next_element:
                sorted_to += 1 # wrong level - temp fix
