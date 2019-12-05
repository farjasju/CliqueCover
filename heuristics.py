import numpy as np
import math
import time
import random
from itertools import combinations
from collections import defaultdict


from helpers import enter_matrix, is_edge, is_in_clique, is_clique, cliques_from_list, is_solution, load_graph, neighbors, find_clique_dumb, triangles
from test_instances import test_graph1, test_graph2, test_graph3


def light_backtrack(adj_mat, cliques, v=1,  best=(math.inf, None)):

    n = adj_mat.shape[0]

    if v == n:
        if is_solution(cliques, adj_mat):
            if len(set(list(cliques))-set({0})) < best[0]:
                best = (len(set(list(cliques))), cliques_from_list(cliques))

    else:
        for i in range(1, v+2):
            cliques[v] = i
            if is_solution(cliques, adj_mat):
                if len(set(list(cliques))-set({0})) < best[0]:
                    best = light_backtrack(adj_mat, cliques, v+1, best)

    return best


def greedy(adj_mat, repetitions=10):
    n = adj_mat.shape[0]
    best = [x for x in range(1, n+1)]
    for r in range(repetitions):
        # print(best)
        vertices = [x for x in range(1, n+1)]
        random.shuffle(vertices)  # random permutation of vertices
        cliques = [0 for x in range(n)]
        sizes = defaultdict(int)  # size of each clique
        sizes[0] = n
        c = 1  # clique names
        for i in range(n):
            v = vertices[i]
            # print(" * Vertice", v)
            labeled = False
            # will count the size of each clique among the neighbors of v:
            neighbors_cliques = defaultdict(int)
            for neighbor in neighbors(v, adj_mat):
                neighbors_cliques[cliques[neighbor-1]] += 1
            for clique, size in neighbors_cliques.items():
                if size == sizes[clique]:
                    # print("S'AJOUTE A LA CLIQUE", clique)
                    cliques[v-1] = clique
                    sizes[clique] += 1
                    labeled = True
                    continue
            if not labeled:
                # print("CREE LA CLIQUE", c)
                cliques[v-1] = c
                sizes[c] += 1
                c += 1
        if len(set(cliques)) < len(set(best)):
            best = cliques
        # print("Neighbors cliques", neighbors_cliques.keys())
    return best


def iterated_greedy(adj_mat, repetitions=10):
    # TODO: GRASP algorithm
    pass


def main():
    test_graph = load_graph('instance2.clq')

    start_time = time.time()
    solution = cliques_from_list(greedy(test_graph))
    print("--- %s seconds ---" % (time.time() - start_time))
    print(len(solution), "cliques:", solution)


if __name__ == "__main__":
    main()
