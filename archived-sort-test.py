# Test file for various algorithms
import sorting as st
import sys
import random
import time

# Initialises arrays between 0-10
def init_small():
    array0 = [6,9,9,1,9,10,6,5,9,10]
    array1 = [0,6,0,1,5,0,4,4,3,4]
    array2 = [3,6,3,2,7,4,3,2,7,8]
    array3 = [8,3,6,5,2,3,9,10,8,4]
    array4 = [2,3,0,9,4,4,8,7,6,5]
    array5 = [6,4,9,7,0,10,0,4,3,10]
    array6 = [8,1,1,0,4,8,5,5,4,5]
    array7 = [7,3,5,0,6,6,9,5,7,4]
    array8 = [5,8,2,8,3,5,5,8,2,3]
    array9 = [1,8,5,1,3,5,6,10,8,7]

    array = [array0, array1, array2, array3, array4,
                 array5, array6, array7, array8, array9]
    return array

# Initialises arrays from 0-100
def init_medium():  # Random.randint(0, 100)
    array10 = [26,33,29,89,66,55,29,65,25,73]
    array11 = [99,31,51,39,84,55,26,70,38,68]
    array12 = [76,42,51,73,47,22,17,34,19,14]
    array13 = [4,83,47,14,47,42,41,44,90,45]
    array14 = [77,74,33,20,18,67,47,12,92,47]
    array15 = [22,65,61,82,30,29,65,26,90,15]
    array16 = [53,67,57,90,16,48,94,24,5,90]
    array17 = [43,67,34,77,5,16,2,75,11,1]
    array18 = [21,32,94,40,83,73,22,47,86,61]
    array19 = [29,18,93,27,45,2,21,8,15,87]

    array = [array10, array11, array12, array13, array14,
                 array15, array16, array17, array18, array19]
    return array

# Initialises arrays from 0-1000
def init_large():  # Random.randint(0, 1000)
    array20 = [285,336,765,181,713,923,427,288,611,622]
    array21 = [60,939,917,291,831,285,452,279,857,832]
    array22 = [737,722,251,415,644,887,248,856,403,302]
    array23 = [869,379,637,618,628,400,137,194,967,891]
    array24 = [617,276,9,168,476,596,304,285,790,996]
    array25 = [660,829,992,455,331,106,290,63,324,871]
    array26 = [126,924,352,487,171,805,993,237,143,129]
    array27 = [823,360,942,446,587,531,182,461,51,387]
    array28 = [38,622,292,48,808,558,35,551,344,851]
    array29 = [307,947,199,326,830,137,443,608,244,384]

    array = [array20, array21, array22, array23, array24,
             array25, array26, array27, array28, array29]
    return array

# 0 is sort-test call
# 1 is help or algorithm name
# 2 is small/medium/large/all

# If entered arguments are broken
def broken_args():
    print("Please ensure the arguments are correct. The argument format is " +
          " 'python test.py _number_of_arrays(0-10)_ _random(boolean)_'. " +
          " The arguments surrounded by underscores are optional.")

def wrong_algorithm():
    print("Please ensure you are correctly calling the algorithm, or ensure it is implemented.")

# Checks the number and validity of entered arguments - return -1 if invalid
def check_for_args():
    if len(sys.argv) > 3:
        return -1

    # Checking argument 2 is a valid int within bounds
    try:
        if len(sys.argv) > 1:
            if int(sys.argv[2]) < 0 or int(sys.argv[2]) > len(arr_array):
                return -1
    except:
        return -1

    # Checking argument 3 is a valid bool
    try:
        if len(sys.argv) > 2:
            bool(sys.argv[3])
    except:
        return -1
    return len(sys.argv)


# Testing sort
def main():
    args = check_for_args()

    if args == -1:    # Invalid entry
        broken_args()
    if args == 2:     # All elements
        for element in arr_array:
            print(st.selection(element))
    if args == 3:     # Number of elements chosen
        for element in range(0, int(sys.argv[2])):
            print(st.selection(arr_array[element]))
    if args == 4:     # Random elements
        if sys.argv[3] == 'True':
            for element in range(0, int(sys.argv[2])):
                print(st.selection(arr_array[random.randint(0, len(arr_array)-1)]))
        else:
            for element in range(0, int(sys.argv[2])):
                print(st.selection(arr_array[element]))


if __name__ == "__main__":
    main()
