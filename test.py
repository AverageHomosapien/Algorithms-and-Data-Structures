# Test file for various algorithms
import sorting as st
import sys
import random
import time

array0 = [2, 5, 2, 3, 5, 7, 1, 8, 4, 16]
array1 = [3, 1, 5, 4, 7, 7, 2, 6, 9, 12]
array2 = [9, 3, 4, 2, 4, 6, 7, 9, 10, 1]
array3 = [2, 1, 4, 3, 9, 8, 2, 2, 3, 14]
array4 = [8, 4, 1, 5, 5, 5, 3, 2, 1, 9]
array5 = [7, 12,4, 3,14, 15,2, 7, 7, 6]
array6 = [2, 1, 3, 3, 2, 1, 2, 3, 4, 2]
array7 = [5, 2, 1,-2, 3, 1, 4, 6, 6, 1]
array8 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
array9 = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]

arr_array = [array0, array1, array2, array3, array4,
             array5, array6, array7, array8, array9]

test_array = []

# Called if entered arguments are broken
# Implement a different sort with 4th argument
def broken_args():
    print("Please ensure the arguments are correct. The argument format is " +
          " 'python test.py _number_of_arrays(0-10)_ _random(boolean)_'. " +
          " The arguments surrounded by underscores are optional.")


# Checks the number and validity of entered arguments - return -1 if invalid
def check_for_args():
    if len(sys.argv) > 4:
        return -1

    # Checking argument 2 is a valid int within bounds
    try:
        if len(sys.argv) > 1:
            if int(sys.argv[1]) < 0 or int(sys.argv[1]) > len(arr_array):
                return -1
    except:
        return -1

    # Checking argument 3 is a valid bool
    try:
        if len(sys.argv) > 2:
            bool(sys.argv[2])
    except:
        return -1
    return len(sys.argv)


# Testing sort
def main():
    args = check_for_args()

    if args == -1:    # Invalid entry
        broken_args()
    if args == 1:     # All elements
        for element in arr_array:
            print(st.selection(element))
    if args == 2:     # Number of elements chosen
        for element in range(0, int(sys.argv[1])):
            print(st.selection(arr_array[element]))
    if args == 3:     # Random elements
        if sys.argv[2] == 'True':
            for element in range(0, int(sys.argv[1])):
                print(st.selection(arr_array[random.randint(0, len(arr_array)-1)]))
        else:
            for element in range(0, int(sys.argv[1])):
                print(st.selection(arr_array[element]))

if __name__ == "__main__":
    main()
