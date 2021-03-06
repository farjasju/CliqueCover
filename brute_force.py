import time
import numpy as np
import math

from helpers import enter_matrix, is_edge, is_in_clique, is_clique, cliques_from_list, is_solution, load_graph
from test_instances import test_graph1, test_graph2, test_graph3


def brute_force(adj_mat, cliques, v=0, best=(math.inf, None)):

    n = adj_mat.shape[0]

    if v == n:
        if is_solution(cliques, adj_mat):
            if len(set(list(cliques))) < best[0]:
                best = (len(set(list(cliques))), cliques_from_list(cliques))

    else:
        for i in range(1, v+2):
            cliques[v] = i
            best = brute_force(adj_mat, cliques, v+1, best)

    return best


def main():
    test_graph, nb_nodes, nb_edges = load_graph(
        'specific/Gnp12_0.2.clq')
    start_time = time.time()
    cliques = [0 for x in range(test_graph.shape[0])]
    cliques[0] = 1
    solution = brute_force(test_graph, cliques, 0)
    print(solution[0], "cliques:", solution[1])
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
