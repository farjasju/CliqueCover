import numpy as np

test_graph1 = np.array([[0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 1, 1],
                        [0, 1, 0, 1, 0, 1],
                        [0, 0, 1, 1, 1, 0]])

test_graph2 = np.array([[0, 1, 0, 1, 1, 0],
                        [1, 0, 1, 0, 1, 0],
                        [0, 1, 0, 1, 1, 1],
                        [1, 0, 1, 0, 1, 1],
                        [1, 1, 1, 1, 0, 1],
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


def is_edge(u, v, adj_mat):
    return adj_mat[u-1, v-1]


def is_in_clique(v, clique, adj_mat):
    is_in = True
    if clique is None:
        return False
    for node in clique:
        if not is_edge(v, node, adj_mat):
            is_in = False
    return is_in


def main():
    enter_matrix()


if __name__ == '__main__':
    main()
