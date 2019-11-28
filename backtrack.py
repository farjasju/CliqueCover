import numpy as np
import math
import time

from helpers import enter_matrix, is_edge, is_in_clique, is_clique, cliques_from_list, is_solution
from test_instances import test_graph1, test_graph2, test_graph3


def backtrack(adj_mat, cliques, v=0,  best=(math.inf, None)):
    n = adj_mat.shape[0]
    print("CALL: v=" + str(v), len(set(list(cliques))), "cliques=", cliques)
    if v == n:
        if is_solution(cliques, adj_mat):
            if len(set(list(cliques))) < best[0]:
                best = (len(set(list(cliques))), cliques_from_list(cliques))
                print('best:', best)
    else:
        for i in range(1, v+2):
            # if nao melhor

            cliques[v] = i
            best = backtrack(adj_mat, cliques, v+1, best)
    return best


def main():
    start_time = time.time()
    cliques = [0 for x in range(test_graph2.shape[0])]
    cliques[0] = 1
    solution = backtrack(test_graph2, cliques, 0)
    print(solution[0], "cliques:", solution[1])
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
