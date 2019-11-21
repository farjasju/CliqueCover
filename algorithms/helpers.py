import numpy as np 

def enter_matrix():
    R = int(input("Enter the number of rows:"))
    C = int(input("Enter the number of columns:"))
    print("Enter the entries in a single line (separated by space): ")
    # User input of entries in a
    # single line separated by space
    entries = list(map(int, input().split()))
    # For printing the matrix
    matrix = np.array(entries).reshape(R, C)
    print(repr(matrix))
    return(matrix)

def main():
    enter_matrix()

if __name__ == '__main__':
    main()