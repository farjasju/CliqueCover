import numpy as np

test_graph = np.array([[0, 0, 0, 1, 0, 0],
                       [0, 0, 0, 0, 1, 0],
                       [0, 0, 0, 0, 0, 1],
                       [1, 0, 0, 0, 1, 1],
                       [0, 1, 0, 1, 0, 1],
                       [0, 0, 1, 1, 1, 0]])


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


def is_in_clique(v, clique, adj_mat):
    pass


def brute_force(adj_mat):
    n = adj_mat.shape[0]
    cliques = {{1}}
    for i in range(1, n+1):
        for clique in cliques:
            if is_in_clique(i, clique, adj_mat):
                pass
            else:
                cliques.add({i})


def main():
    brute_force()


if __name__ == "__main__":
    main()
