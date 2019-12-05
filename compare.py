import numpy as np
import math
import time

from backtrack import backtrack
from brute_force import brute_force
from heuristics import greedy, greedy2
from helpers import load_graph, cliques_from_list
from test_instances import test_graph1, test_graph2


def main():
    test_graph, nb_nodes, nb_edges = load_graph(
        'specific/Gnp10_0.2.clq')

    print("\n--- GREEDY ---")
    start_time = time.time()
    gd_solution = cliques_from_list(greedy(test_graph))
    print(">>> %s seconds" % (time.time() - start_time))
    print(">>>", len(gd_solution), "cliques")
    print(">>>", gd_solution)

    print("\n--- BACKTRACK ---")
    start_time = time.time()
    cliques = [0 for x in range(test_graph.shape[0])]
    cliques[0] = 1
    bt_solution = backtrack(test_graph, cliques, 1)
    print(">>> %s seconds" % (time.time() - start_time))
    print(">>>", bt_solution[0], "cliques")
    print(">>>", bt_solution[1])

    print("\n--- BRUTE FORCE ---")
    start_time = time.time()
    bf_solution = brute_force(test_graph, cliques, 0)
    print(">>> %s seconds" % (time.time() - start_time))
    print(">>>", bf_solution[0], "cliques")
    print(">>>", bf_solution[1])


if __name__ == '__main__':
    main()
