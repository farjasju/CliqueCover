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

def is_edge(u,v, adj_mat):
    return adj_mat[u-1,v-1]


def is_in_clique(v, clique, adj_mat):
    is_in = True
    if clique is None:
        return False
    for node in clique:
        if not is_edge(v, node, adj_mat):
            is_in = False
    return is_in


def brute_force(adj_mat, v, cliques):
    '''To be initialized with node 1 and its clique'''
    print("entering node", v, "with cliques", cliques)
    n = adj_mat.shape[0]
    if v > n:
        return cliques
    added_to_clique = False
    for c in list(cliques):
        clique = cliques[c]
        print("  checking", v, clique)
        if is_in_clique(v, clique, adj_mat):
            print("  VERIFIED", v, "in clique", c, clique)
            cliques[c].add(v)
            added_to_clique = True
            continue
    if not added_to_clique:
        print("  CREATING clique", v)
        cliques[v] = set([v]) # the clique is named after its first node
    return brute_force(adj_mat, v+1, cliques)

def main():
    cliques = dict()
    cliques[1] = set([1])
    print("cliques:", brute_force(test_graph, 1, cliques))


if __name__ == "__main__":
    main()
