import numpy as np
import math
import time

from backtrack import backtrack
from brute_force import brute_force
from heuristics import greedy2
from helpers import load_graph, cliques_from_list


def main():
    test_graph = load_graph('instance5.clq')

    start_time = time.time()
    cliques = [0 for x in range(test_graph.shape[0])]
    cliques[0] = 1
    solution = backtrack(test_graph, cliques, 0)
    print(solution[0], "cliques:", solution[1])
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    solution = cliques_from_list(greedy2(test_graph))
    print(len(solution), "cliques:", solution)
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()
