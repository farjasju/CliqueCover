import matplotlib.pyplot as plt
import numpy as np
import math
import time
from datetime import datetime
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
    now = datetime.now().strftime("%d_%m_%Y_%I_%M_%S")

    # if true, compares at a fixed number of nodes. If false, compares at a fixed probability of edges.
    n_constant = False

    generate_graphs(n=20, p=0.15, start=4, stop=20,
                    nb=30, n_constant=n_constant)

    if not os.path.exists(OUT_DIR):
        os.mkdir(OUT_DIR)

    with open(os.path.join(OUT_DIR, 'results_' + now + '.csv'), 'w') as output_file:
        fieldnames = ['nodes', 'edges', 'greedy_duration', 'greedy_solution',
                      'backtrack_duration', 'backtrack_solution', 'lt_backtrack_duration', 'lt_backtrack_solution']
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()

        results_by_edge = dict()
        results_by_node = dict()

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

            results_by_edge[nb_edges] = {'greedy_duration': greedy_duration, 'greedy_solution': greedy_solution,
                                         'backtrack_duration': backtrack_duration, 'backtrack_solution': backtrack_solution,
                                         'lt_backtrack_duration': lt_backtrack_duration, 'lt_backtrack_solution': lt_backtrack_solution}
            results_by_node[nb_nodes] = {'greedy_duration': greedy_duration, 'greedy_solution': greedy_solution,
                                         'backtrack_duration': backtrack_duration, 'backtrack_solution': backtrack_solution,
                                         'lt_backtrack_duration': lt_backtrack_duration, 'lt_backtrack_solution': lt_backtrack_solution}

            row = dict({'nodes': nb_nodes, 'edges': nb_edges, 'greedy_duration': greedy_duration, 'greedy_solution': greedy_solution,
                        'backtrack_duration': backtrack_duration, 'backtrack_solution': backtrack_solution,
                        'lt_backtrack_duration': lt_backtrack_duration, 'lt_backtrack_solution': lt_backtrack_solution})
            writer.writerow(row)

    if not n_constant:
        nodes_numbers = []
        edges_numbers = []
        greedy_durations = []
        greedy_solutions = []
        backtrack_durations = []
        backtrack_solutions = []
        lt_backtrack_durations = []
        lt_backtrack_solutions = []

        for n in sorted(results_by_node.keys()):
            nodes_numbers.append(n)
            greedy_durations.append(results_by_node[n]['greedy_duration'])
            greedy_solutions.append(results_by_node[n]['greedy_solution'])
            backtrack_durations.append(
                results_by_node[n]['backtrack_duration'])
            backtrack_solutions.append(
                results_by_node[n]['backtrack_solution'])
            lt_backtrack_durations.append(
                results_by_node[n]['lt_backtrack_duration'])
            lt_backtrack_solutions.append(
                results_by_node[n]['lt_backtrack_solution'])

        plt.rcParams["figure.figsize"] = (18, 12)
        plt.title("Algorithm duration given the number of nodes of the graph")
        plt_values = pd.DataFrame(
            {'nodes': nodes_numbers, 'greedy_duration': greedy_durations, 'backtrack_duration': backtrack_durations, 'lt_backtrack_duration': lt_backtrack_durations})
        plt.xlabel("Number of nodes")
        plt.ylabel("Seconds")
        plt.plot('nodes', 'greedy_duration', data=plt_values,
                 lw=2, label='Greedy algorithm')
        plt.plot('nodes', 'backtrack_duration', data=plt_values,
                 lw=2, label='Backtracking algorithm')
        plt.legend()
        plt.savefig(os.path.join(OUT_DIR, 'durations_nodes_' +
                                 now + '.png'), bbox_inches="tight")
        # plt.show()
        plt.clf()

        plt.title("Number of cliques found given the number of nodes of the graph")
        plt_values = pd.DataFrame(
            {'nodes': nodes_numbers, 'greedy_solutions': greedy_solutions, 'backtrack_solutions': backtrack_solutions, 'lt_backtrack_solutions': lt_backtrack_solutions})
        plt.xlabel("Number of nodes")
        plt.ylabel("Number of cliques found")
        plt.plot('nodes', 'greedy_solutions', data=plt_values,
                 lw=2, label='Greedy algorithm')
        plt.plot('nodes', 'backtrack_solutions', data=plt_values,
                 lw=2, label='Backtracking algorithm')
        plt.legend()
        plt.savefig(os.path.join(OUT_DIR, 'solutions_nodes_' +
                                 now + '.png'), bbox_inches="tight")
        # plt.show()
        plt.clf()

        ratios = []
        for i in range(len(greedy_solutions)):
            ratios.append(greedy_solutions[i]/backtrack_solutions[i])

        plt.title(
            "Ratio of number of cliques found given the number of nodes of the graph")
        plt_values = pd.DataFrame(
            {'nodes': nodes_numbers, 'ratio': ratios})
        plt.xlabel("Number of nodes")
        plt.ylabel("Ratio greedy/backtrack")
        plt.plot('nodes', 'ratio', data=plt_values,
                 lw=2)
        plt.savefig(os.path.join(OUT_DIR, 'ratio_nodes_' +
                                 now + '.png'), bbox_inches="tight")
        # plt.show()
        plt.clf()

    nodes_numbers = []
    edges_numbers = []
    greedy_durations = []
    greedy_solutions = []
    backtrack_durations = []
    backtrack_solutions = []
    lt_backtrack_durations = []
    lt_backtrack_solutions = []

    for m in sorted(results_by_edge.keys()):
        edges_numbers.append(m)
        greedy_durations.append(results_by_edge[m]['greedy_duration'])
        greedy_solutions.append(results_by_edge[m]['greedy_solution'])
        backtrack_durations.append(results_by_edge[m]['backtrack_duration'])
        backtrack_solutions.append(results_by_edge[m]['backtrack_solution'])
        lt_backtrack_durations.append(
            results_by_edge[m]['lt_backtrack_duration'])
        lt_backtrack_solutions.append(
            results_by_edge[m]['lt_backtrack_solution'])

    plt.rcParams["figure.figsize"] = (18, 8)
    plt.title("Algorithm duration given the number of edges of the graph")
    plt_values = pd.DataFrame(
        {'edges': edges_numbers, 'greedy_duration': greedy_durations, 'backtrack_duration': backtrack_durations, 'lt_backtrack_duration': lt_backtrack_durations})
    plt.xlabel("Number of edges")
    plt.ylabel("Seconds")
    plt.plot('edges', 'greedy_duration', data=plt_values,
             lw=2, label='Greedy algorithm')
    plt.plot('edges', 'backtrack_duration', data=plt_values,
             lw=2, label='Backtracking algorithm')
    plt.legend()
    plt.savefig(os.path.join(OUT_DIR, 'durations_edges_' +
                             now + '.png'), bbox_inches="tight")
    # plt.show()
    plt.clf()

    plt.title("Number of cliques found given the number of edges of the graph")
    plt_values = pd.DataFrame(
        {'edges': edges_numbers, 'greedy_solutions': greedy_solutions, 'backtrack_solutions': backtrack_solutions, 'lt_backtrack_solutions': lt_backtrack_solutions})
    plt.xlabel("Number of edges")
    plt.ylabel("Number of cliques found")
    plt.plot('edges', 'greedy_solutions', data=plt_values,
             lw=2, label='Greedy algorithm')
    plt.plot('edges', 'backtrack_solutions', data=plt_values,
             lw=2, label='Backtracking algorithm')
    plt.legend()
    plt.savefig(os.path.join(OUT_DIR, 'solutions_edges_' +
                             now + '.png'), bbox_inches="tight")
    # plt.show()
    plt.clf()

    ratios = []
    for i in range(len(greedy_solutions)):
        ratios.append(greedy_solutions[i]/backtrack_solutions[i])

    plt.title(
        "Ratio of number of cliques found given the number of edges of the graph")
    plt_values = pd.DataFrame(
        {'edges': edges_numbers, 'ratio': ratios})
    plt.xlabel("Number of edges")
    plt.ylabel("Ratio greedy/backtrack")
    plt.plot('edges', 'ratio', data=plt_values,
             lw=2)
    plt.savefig(os.path.join(OUT_DIR, 'ratio_edges_' +
                             now + '.png'), bbox_inches="tight")
    # plt.show()
    plt.clf()


if __name__ == '__main__':
    main()
