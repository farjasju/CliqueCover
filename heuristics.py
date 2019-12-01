import numpy as np
import math
import time
import random
from itertools import combinations
from collections import defaultdict


from helpers import enter_matrix, is_edge, is_in_clique, is_clique, cliques_from_list, is_solution, load_graph, neighbors, find_clique_dumb, triangles
from test_instances import test_graph1, test_graph2, test_graph3


def greedy1(adj_mat, cliques, v=0,  best=(math.inf, None)):
    n = adj_mat.shape[0]
    start_node = random.randint(1, n)
    cliques = [0 for x in range(n)]
    current_node = start_node
    remaining_nodes = set([x for x in range(1, n+1)])
    i = 1
    while remaining_nodes:
        clique = {'name': i, 'nodes': set([current_node])}
        neighbors = neighbors(current_node)
        for neighbor in neighbors:
            if is_clique(clique['nodes'].union([neighbor])):
                cliques[neighbor] = clique['name']
    return best


def greedy2(adj_mat, tries=5, best=(math.inf, None)):
    n = adj_mat.shape[0]
    for t in range(tries):
        start_node = random.randint(1, n)
        cliques = [0 for x in range(n)]
        current_node = start_node
        remaining_nodes = set([x for x in range(1, n+1)])
        remaining_nodes.remove(start_node)
        i = 1
        while remaining_nodes:
            # print(remaining_nodes, 'cliques:', cliques_from_list(cliques))
            clique = {'name': i, 'nodes': set([current_node])}
            cn_neighbors = neighbors(current_node, adj_mat)
            # print('node:', current_node, 'neighbors:', cn_neighbors)
            for neighbor in cn_neighbors:
                new_clique = clique['nodes'].union([neighbor])
                if is_clique(new_clique, adj_mat):
                    cliques[neighbor-1] = clique['name']
                    cliques[current_node-1] = clique['name']
                    for node in range(1, n+1):
                        if is_in_clique(node, new_clique, adj_mat):
                            cliques[node-1] = clique['name']
                            new_clique.add(node)
                    # remaining_nodes.remove(neighbor)
                    # print('clique:', clique['nodes'].union([neighbor]))
                    break
            current_node = remaining_nodes.pop()
            i = i + 1
        if len(cliques_from_list(cliques)) < best[0]:
            best = (len(cliques_from_list(cliques)), cliques)
    return cliques


def greedy3(adj_mat):
    n = adj_mat.shape[0]
    cliques = [0 for x in range(n)]
    nodes = set([x for x in range(1, n+1)])
    i = 1
    for l in range(n):
        node = nodes.pop()
        print('node', node)
        for (neighb1, neighb2) in combinations(neighbors(node, adj_mat), 2):
            if is_edge(neighb1, neighb2, adj_mat):
                clique = set([node, neighb1, neighb2])
                for x in clique:
                    cliques[x-1] = i
                for outer_neighb in (set(neighbors(clique, adj_mat))-clique):
                    if is_clique(clique.union({outer_neighb}), adj_mat):
                        clique.add(outer_neighb)
                        cliques[outer_neighb-1] = i
    return cliques


def greedy(adj_mat, repetitions=10):
    n = adj_mat.shape[0]
    best = [x for x in range(n)]
    for r in range(repetitions):
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


def triangle_search(adj_mat):
    n = adj_mat.shape[0]
    return triangles(adj_mat)


def main():
    test_graph = load_graph('instance2.clq')

    start_time = time.time()
    solution = cliques_from_list(greedy2(test_graph))
    print("--- %s seconds ---" % (time.time() - start_time))
    print(len(solution), "cliques:", solution)

    start_time = time.time()
    solution = cliques_from_list(greedy3(test_graph))
    print("--- %s seconds ---" % (time.time() - start_time))
    print(len(solution), "cliques:", solution)

    start_time = time.time()
    solution = triangle_search(test_graph)
    print("--- %s seconds ---" % (time.time() - start_time))
    print(len(solution), "cliques:", solution)


if __name__ == "__main__":
    main()