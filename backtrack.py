import numpy as np

from helpers import enter_matrix, is_edge, is_in_clique
from test_instances import test_graph1, test_graph2, test_graph3


def backtrack(adj_mat, v, cliques, best):
    '''To be initialized with node 1 and its clique'''
    print("entering node", v, "with cliques", cliques)
    n = adj_mat.shape[0]
    nb_cliques = len(cliques)
    if v > n:
        if nb_cliques < best:
            best = nb_cliques
            return nb_cliques, cliques
    else:
        for c in list(cliques):
            clique = cliques[c]
            print("  checking", v, clique)
            if is_in_clique(v, clique, adj_mat):
                print("  VERIFIED", v, "in clique", c, clique)
                cliques[c].add(v)
                best = backtrack(adj_mat, v+1, cliques, nb_cliques)
        else:
            print("  CREATING clique", v)
            cliques[v] = set([v])  # the clique is named after its first node
            best = backtrack(adj_mat, v+1, cliques, nb_cliques)
    return best


def main():
    cliques = dict()
    cliques[1] = set([1])
    print("cliques:", backtrack(test_graph1, 1, cliques, 10000))


if __name__ == "__main__":
    main()
