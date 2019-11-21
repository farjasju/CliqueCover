import numpy as np

from helpers import test_graph1, test_graph2, enter_matrix, is_edge, is_in_clique


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
        cliques[v] = set([v])  # the clique is named after its first node
    return brute_force(adj_mat, v+1, cliques)


def main():
    cliques = dict()
    cliques[1] = set([1])
    print("cliques:", brute_force(test_graph2, 1, cliques))


if __name__ == "__main__":
    main()
