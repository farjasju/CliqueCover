import numpy as np
import math
import time

from backtrack import backtrack
from brute_force import brute_force
from heuristics import greedy, greedy2
from helpers import load_graph, cliques_from_list
from test_instances import test_graph1, test_graph2


def main():
    test_graph = load_graph('instance3.clq')

    print("\n--- GREEDY ---")
    start_time = time.time()
    solution = cliques_from_list(greedy(test_graph))
    print("--- %s seconds ---" % (time.time() - start_time))
    print(">>>", len(solution), "cliques")

    print("\n--- BACKTRACK ---")
    start_time = time.time()
    cliques = [0 for x in range(test_graph.shape[0])]
    cliques[0] = 1
    solution = backtrack(test_graph, cliques, 0)
    print("--- %s seconds ---" % (time.time() - start_time))
    print(">>>", solution[0], "cliques")

    print("\n--- GREEDY2 ---")
    start_time = time.time()
    solution = cliques_from_list(greedy2(test_graph))
    print("--- %s seconds ---" % (time.time() - start_time))
    print(">>>", len(solution), "cliques")


if __name__ == '__main__':
    main()
