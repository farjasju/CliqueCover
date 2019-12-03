import matplotlib.pyplot as plt
import numpy as np
import math
import time
import os
import csv
import pandas as pd

from collections import OrderedDict

from backtrack import backtrack
from brute_force import brute_force
from heuristics import greedy, greedy2, light_backtrack
from helpers import load_graph, cliques_from_list
from random_graph_generator import generate_graphs

OUT_DIR = os.path.join('data', 'benchmark_results')
DATA_DIR = os.path.join('data', 'random_graphs', 'clq')


def main():
    generate_graphs(p=0.2, start=5, stop=20, nb=20)

    if not os.path.exists(OUT_DIR):
        os.mkdir(OUT_DIR)

    with open(os.path.join(OUT_DIR, 'results.csv'), 'w') as output_file:
        fieldnames = ['nodes', 'edges', 'greedy_duration', 'greedy_solution',
                      'backtrack_duration', 'backtrack_solution']
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()

        results = dict()

        for file in os.listdir(DATA_DIR):
            print('\n')
            graph, nb_nodes, nb_edges = load_graph(
                os.path.join('random_graphs', 'clq', file))
            # print(nb_nodes, 'nodes', nb_edges, 'edges')
            start_time = time.time()
            gd_solution = cliques_from_list(greedy(graph))
            greedy_duration = time.time() - start_time
            greedy_solution = len(gd_solution)
            print('GREEDY:', greedy_solution, 'cliques', greedy_duration, 's')

            cliques = [0 for x in range(graph.shape[0])]
            cliques[0] = 1
            start_time = time.time()
            ltbt_solution = light_backtrack(graph, cliques, 1)
            lt_backtrack_duration = time.time() - start_time
            lt_backtrack_solution = ltbt_solution[0]
            print('LIGHT BACKTRACK:', lt_backtrack_solution,
                  'cliques', lt_backtrack_duration, 's')

            start_time = time.time()
            bt_solution = backtrack(graph, cliques, 1)
            backtrack_duration = time.time() - start_time
            backtrack_solution = bt_solution[0]
            print('BACKTRACK:', backtrack_solution,
                  'cliques', backtrack_duration, 's')

            # start_time = time.time()
            # bf_solution = brute_force(graph, cliques, 0)
            # bf_duration = time.time() - start_time
            # print('BRUTE FORCE:', bf_solution[0], 'cliques', bf_duration, 's')

            # DEBUG
            if greedy_solution < backtrack_solution:
                print('HMMM', nb_nodes, 'nodes', 'greedy:',
                      gd_solution, 'backtrack:', bt_solution[1])
                print(graph)
                if nb_nodes < 10:
                    bf_solution = brute_force(graph, cliques, 0)
                    print('BRUTE FORCE:',
                          bf_solution[0], 'cliques', bf_solution[1])

            results[nb_nodes] = {'greedy_duration': greedy_duration, 'greedy_solution': greedy_solution,
                                 'backtrack_duration': backtrack_duration, 'backtrack_solution': backtrack_solution}

            row = dict({'nodes': nb_nodes, 'edges': nb_edges, 'greedy_duration': greedy_duration, 'greedy_solution': greedy_solution,
                        'backtrack_duration': backtrack_duration, 'backtrack_solution': backtrack_solution})
            writer.writerow(row)

    nodes_numbers = []
    greedy_durations = []
    greedy_solutions = []
    backtrack_durations = []
    backtrack_solutions = []

    for n in sorted(results.keys()):
        nodes_numbers.append(n)
        greedy_durations.append(results[n]['greedy_duration'])
        greedy_solutions.append(results[n]['greedy_solution'])
        backtrack_durations.append(results[n]['backtrack_duration'])
        backtrack_solutions.append(results[n]['backtrack_solution'])

    plt.rcParams["figure.figsize"] = (18, 8)
    plt.title("Algorithm duration given the number of nodes of the graph")
    plt_values = pd.DataFrame(
        {'nodes': nodes_numbers, 'greedy_duration': greedy_durations, 'backtrack_duration': backtrack_durations})
    plt.xlabel("Number of nodes")
    plt.ylabel("Seconds")
    plt.plot('nodes', 'greedy_duration', data=plt_values,
             lw=2, label='Greedy algorithm')
    plt.plot('nodes', 'backtrack_duration', data=plt_values,
             lw=2, label='Backtracking algorithm')
    plt.legend()
    plt.savefig(os.path.join(OUT_DIR, 'durations.png'), bbox_inches="tight")
    plt.show()
    plt.clf()

    plt.title("Number of cliques found given the number of nodes of the graph")
    plt_values = pd.DataFrame(
        {'nodes': nodes_numbers, 'greedy_solutions': greedy_solutions, 'backtrack_solutions': backtrack_solutions})
    plt.xlabel("Number of nodes")
    plt.ylabel("Number of cliques found")
    plt.plot('nodes', 'greedy_solutions', data=plt_values,
             lw=2, label='Greedy algorithm')
    plt.plot('nodes', 'backtrack_solutions', data=plt_values,
             lw=2, label='Backtracking algorithm')
    plt.legend()
    plt.savefig(os.path.join(OUT_DIR, 'solutions.png'), bbox_inches="tight")
    plt.show()


if __name__ == '__main__':
    main()
