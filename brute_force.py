import numpy as np
import math

from helpers import enter_matrix, is_edge, is_in_clique, is_clique, cliques_from_list
from test_instances import test_graph1, test_graph2, test_graph3

# def brute_force_old(adj_mat, v, cliques):
#     '''To be initialized with node 1 and its clique'''
#     print("entering node", v, "with cliques", cliques)
#     n = adj_mat.shape[0]
#     if v > n:
#         return cliques
#     added_to_clique = False
#     for c in list(cliques):
#         clique = cliques[c]
#         print("  checking", v, clique)
#         if is_in_clique(v, clique, adj_mat):
#             print("  VERIFIED", v, "in clique", c, clique)
#             cliques[c].add(v)
#             added_to_clique = True
#             continue
#     if not added_to_clique:
#         print("  CREATING clique", v)
#         cliques[v] = set([v])  # the clique is named after its first node
#     return brute_force_old(adj_mat, v+1, cliques)

# cliques = [1 1 1 4 4 6 6 1 1 8 ...] |V|


def is_solution(nodes_list, adj_mat, v=None):
    "Verifies if the cliques in x up to v are indeed cliques"
    if v is None:
        v = adj_mat.shape[0]
    cliques_dict = cliques_from_list(nodes_list, v)
    for clique_nodes in cliques_dict.values():
        if not is_clique(clique_nodes, adj_mat):
            return False
    # print("IS SOLUTION :", cliques_from_list(nodes_list))
    return True


def brute_force(adj_mat, cliques, v=0, best=(math.inf, None)):
    n = adj_mat.shape[0]
    print("CALL: v=" + str(v), len(set(list(cliques))), "cliques=", cliques)
    if v == n:
        if is_solution(cliques, adj_mat, v):
            if len(set(list(cliques))) < best[0]:
                best = (len(set(list(cliques))), cliques_from_list(cliques))
                print('best:', best)
    else:
        for i in range(1, v+2):
            cliques[v] = i
            best = brute_force(adj_mat, cliques, v+1, best)
    return best


def main():
    cliques = [0 for x in range(test_graph3.shape[0])]
    cliques[0] = 1
    solution = brute_force(test_graph3, cliques, 0)
    print(solution[0], "cliques:", solution[1])


if __name__ == "__main__":
    main()
