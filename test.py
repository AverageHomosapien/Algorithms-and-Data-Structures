# Test file to test the various algorithms
import sorting as st

array1 = [3, 1, 5, 4, 7, 7, 2, 6, 9, 12]
array2 = [9, 3, 4, 2, 4, 6, 7, 9, 10, 1]
array3 = [2, 1, 4, 3, 9, 8, 2, 2, 3, 14]

arr_array = [array1, array2, array3]

def main():
    for arr in arr_array:
        print(st.selection(arr))

if __name__ == "__main__":
    main()
