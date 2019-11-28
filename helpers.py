import numpy as np
from itertools import combinations


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


def is_clique(nodes, adj_mat):
    for (node_i, node_j) in combinations(nodes, 2):
        if not is_edge(node_i, node_j, adj_mat):
            return False
    # if len(nodes) > 1:
    #     print("IS CLIQUE", nodes)
    return True


def is_edge(u, v, adj_mat):
    # print("EDGE", u, v, bool(adj_mat[u-1, v-1]))
    return adj_mat[u-1, v-1]


def is_in_clique(v, clique, adj_mat):
    is_in = True
    if clique is None:
        return False
    for node in clique:
        if not is_edge(v, node, adj_mat):
            is_in = False
    return is_in


def is_solution(nodes_list, adj_mat, v=None):
    "Verifies if the cliques in x up to v are indeed cliques"
    if v is None:
        v = adj_mat.shape[0]
    cliques_dict = cliques_from_list(nodes_list, v)
    for clique_nodes in cliques_dict.values():
        if not is_clique(clique_nodes, adj_mat):
            return False
    return True


def cliques_from_list(nodes_list, v=None):
    '''Takes the list X = [1 1 2 3 3 ... ] of nodes containing the label of their associated clique, and returns a dict of the different cliques'''
    if v is None:
        v = len(nodes_list)
    cliques = dict()
    for i in range(v):
        clique = nodes_list[i]
        if clique in list(cliques):
            cliques[clique].add(i+1)
        else:
            cliques[clique] = set([i+1])
    return cliques


def main():
    enter_matrix()


if __name__ == '__main__':
    main()
