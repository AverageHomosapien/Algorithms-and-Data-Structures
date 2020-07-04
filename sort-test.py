# Test file for various algorithms
import sort as st
import sys
import random
import time

'''
Program input:
python sort-test.py _algorithm_(string (name)) _tests_(int (0-4))
You can also leave out all parameters for function help

Parameter 1: Name of Algorithm / Empty for help
Parameter 2: 1: small, 2: medium, 3: large, 0: all
'''


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

    temp_array = [array0, array1, array2, array3, array4,
            array5, array6, array7, array8, array9]
    return temp_array


# Initialises arrays from 0-100
def init_medium():
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

    temp_array = [array10, array11, array12, array13, array14,
                 array15, array16, array17, array18, array19]
    return temp_array


# Initialises arrays from 0-1000
def init_large():
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

    temp_array = [array20, array21, array22, array23, array24,
                array25, array26, array27, array28, array29]
    return temp_array


# Initialises all arrays
def init_all():
    small_arr = init_small()
    med_arr = init_medium()
    large_arr = init_large()

    full_array = small_arr + med_arr + large_arr
    return full_array


# Dictionary mapping sort algorithms to user input
sort_dict = {'selection': st.selection, 'insertion': st.insertion}

# Dictionary mapping benchmark test suite to user input
size_dict = {1: 'small', 2: 'medium', 3: 'large', 0: 'all'}

# Error message
def broken_args():
    print("Please ensure the arguments are correct")
    help()

# Error message
def wrong_algorithm():
    print("Please ensure you are correctly calling the algorithm, or ensure it is implemented.")
    help()

# Provides help with the function
def help():
    print("The argument format is python sort-test.py _algorithm_(string (name)) "+
        "_tests_(int (0-4)). The test argument is optional. You can find information "+
        "on the algorithms that have been implemented in the algorithms.md file")


# Checks the count and validity of CLI arguments - return negative if invalid
def check_for_args():
    if len(sys.argv) > 3:
        return -1

    try:  # Checking chosen algorithm is valid
        if len(sys.argv) > 1:
            if sys.argv[1].lower() not in sort_dict:
                return -2
    except:
        return -1

    try: # Checking chosen tests are valid (small/medium/large/all)
        if len(sys.argv) > 2:
            if int(sys.argv[2]) not in size_dict:
                return -1
    except:
        return -1
    return len(sys.argv)


# Testing sort
def main():
    args = check_for_args()
    sort_array = []
    if args > 2: # If argument entered
        if size_dict[int(sys.argv[2])] == 'small':
            sort_array = init_small()
        elif size_dict[int(sys.argv[2])] == 'medium':
            sort_array = init_medium()
        elif size_dict[int(sys.argv[2])] == 'large':
            sort_array = init_large()
        else:
            sort_array = init_all()
    else:
        sort_array = init_small()

    if args == -2:
        wrong_algorithm()
    elif args == -1:    # Invalid entry
        broken_args()
    elif args == 1:
        print("This is the help feature with the sort-test.")
        help()
    elif args == 2:     # Small elements - Algorithm name given
        for element in sort_array:
            print(sort_dict[sys.argv[1]](element))
    elif args == 3:     # Number of elements chosen
        for element in sort_array:
            print(sort_dict[sys.argv[1]](element))

if __name__ == "__main__":
    main()
