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
DATA_DIR = os.path.join('data', 'random_graphs', 'complexity', 'clq')


def main():
    now = datetime.now().strftime("%d_%m_%Y_%I_%M_%S")

    # if true, compares at a fixed number of nodes. If false, compares at a fixed probability of edges.
    n_constant = False

    # generate_graphs(n=20, p=0.15, start=4, stop=20,
    #                 nb=30, n_constant=n_constant)

    if not os.path.exists(OUT_DIR):
        os.mkdir(OUT_DIR)

    with open(os.path.join(OUT_DIR, 'results_' + now + '.csv'), 'w') as output_file:
        fieldnames = ['nodes', 'edges', 'greedy_duration', 'greedy_solution']
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()

        results_by_edge = dict()
        results_by_node = dict()

        for file in os.listdir(DATA_DIR):
            print('\n')
            graph, nb_nodes, nb_edges = load_graph(
                os.path.join('random_graphs', 'complexity', 'clq', file))
            # print(nb_nodes, 'nodes', nb_edges, 'edges')
            start_time = time.time()
            gd_solution = cliques_from_list(greedy(graph))
            greedy_duration = time.time() - start_time
            greedy_solution = len(gd_solution)
            print('GREEDY:', greedy_solution, 'cliques', greedy_duration, 's')

            results_by_edge[nb_edges] = {
                'greedy_duration': greedy_duration, 'greedy_solution': greedy_solution}
            results_by_node[nb_nodes] = {
                'greedy_duration': greedy_duration, 'greedy_solution': greedy_solution}

            row = dict({'nodes': nb_nodes, 'edges': nb_edges,
                        'greedy_duration': greedy_duration, 'greedy_solution': greedy_solution})
            writer.writerow(row)

    if not n_constant:
        nodes_numbers = []
        edges_numbers = []
        greedy_durations = []
        greedy_solutions = []

        for n in sorted(results_by_node.keys()):
            nodes_numbers.append(n)
            greedy_durations.append(results_by_node[n]['greedy_duration'])
            greedy_solutions.append(results_by_node[n]['greedy_solution'])

        #     ratio = []
        #     x_squared = [0.001*x*x for x in nodes_numbers]

        #     plt.rcParams["figure.figsize"] = (18, 12)
        #     plt.title("Algorithm duration given the number of nodes of the graph")
        #     plt_values = pd.DataFrame(
        #         {'nodes': nodes_numbers, 'greedy_duration': greedy_durations, 'x': ratio, 'x_squared': x_squared})
        #     plt.xlabel("Number of nodes")
        #     plt.ylabel("Seconds")
        #     plt.plot('nodes', 'greedy_duration', data=plt_values,
        #              lw=2, label='Greedy algorithm')
        #     plt.plot('nodes', 'nodes', data=plt_values,
        #              lw=2, label='n')
        #     plt.plot('nodes', 'x_squared', data=plt_values,
        #              lw=2, label='n**2')
        #     # plt.plot('nodes', 'lt_backtrack_duration', data=plt_values,
        #     #          lw=2, label='Broken backtracking heuristic')
        #     plt.legend()
        #     plt.savefig(os.path.join(OUT_DIR, 'durations_nodes_' +
        #                              now + '.png'), bbox_inches="tight")
        #     # plt.show()
        #     plt.clf()

        # plt.title("Number of cliques found given the number of nodes of the graph")
        # plt_values = pd.DataFrame(
        #     {'nodes': nodes_numbers, 'greedy_solutions': greedy_solutions, 'backtrack_solutions': backtrack_solutions, 'lt_backtrack_solutions': lt_backtrack_solutions})
        # plt.xlabel("Number of nodes")
        # plt.ylabel("Number of cliques found")
        # plt.plot('nodes', 'greedy_solutions', data=plt_values,
        #          lw=2, label='Greedy algorithm')
        # plt.plot('nodes', 'backtrack_solutions', data=plt_values,
        #          lw=2, label='Backtracking algorithm')
        # # plt.plot('nodes', 'lt_backtrack_solutions', data=plt_values,
        # #          lw=2, label='Broken backtracking heuristic')
        # plt.legend()
        # plt.savefig(os.path.join(OUT_DIR, 'solutions_nodes_' +
        #                          now + '.png'), bbox_inches="tight")
        # # plt.show()
        # plt.clf()
        plt.rcParams["figure.figsize"] = (18, 12)

        ratios = []
        for i in range(len(greedy_solutions)):
            ratios.append(greedy_solutions[i]/nodes_numbers[i])

        plt.title(
            "Ratio of the greedy algorithm duration / number of nodes")
        plt_values = pd.DataFrame(
            {'nodes': nodes_numbers, 'ratio': ratios})
        plt.xlabel("Number of nodes")
        plt.ylabel("Ratio greedy/n")
        plt.plot('nodes', 'ratio', data=plt_values,
                 lw=2,  label='greedy/n')
        plt.legend()
        plt.savefig(os.path.join(OUT_DIR, 'ratio_nodes_' +
                                 now + '.png'), bbox_inches="tight")
        # plt.show()
        plt.clf()

    nodes_numbers = []
    edges_numbers = []
    greedy_durations = []
    greedy_solutions = []
    for m in sorted(results_by_edge.keys()):
        edges_numbers.append(m)
        greedy_durations.append(results_by_edge[m]['greedy_duration'])
        greedy_solutions.append(results_by_edge[m]['greedy_solution'])

    # x_squared = [0.001*x*x for x in edges_numbers]

    # plt.rcParams["figure.figsize"] = (18, 8)
    # plt.title("Algorithm duration given the number of edges of the graph")
    # plt_values = pd.DataFrame(
    #     {'edges': edges_numbers, 'greedy_duration': greedy_durations, 'x_squared': x_squared})
    # plt.xlabel("Number of edges")
    # plt.ylabel("Seconds")
    # plt.plot('edges', 'greedy_duration', data=plt_values,
    #          lw=2, label='Greedy algorithm')
    # plt.plot('edges', 'edges', data=plt_values,
    #          lw=2, label='m')
    # plt.plot('edges', 'x_squared', data=plt_values,
    #          lw=2, label='m**2')
    # # plt.plot('edges', 'lt_backtrack_duration', data=plt_values,
    # #          lw=2, label='Broken backtracking heuristic')
    # plt.legend()
    # plt.savefig(os.path.join(OUT_DIR, 'durations_edges_' +
    #                          now + '.png'), bbox_inches="tight")
    # # plt.show()
    # plt.clf()

    # plt.title("Number of cliques found given the number of edges of the graph")
    # plt_values = pd.DataFrame(
    #     {'edges': edges_numbers, 'greedy_solutions': greedy_solutions, 'backtrack_solutions': backtrack_solutions, 'lt_backtrack_solutions': lt_backtrack_solutions})
    # plt.xlabel("Number of edges")
    # plt.ylabel("Number of cliques found")
    # plt.plot('edges', 'greedy_solutions', data=plt_values,
    #          lw=2, label='Greedy algorithm')
    # plt.plot('edges', 'backtrack_solutions', data=plt_values,
    #          lw=2, label='Backtracking algorithm')
    # # plt.plot('edges', 'lt_backtrack_solutions', data=plt_values,
    # #          lw=2, label='Broken backtracking heuristic')
    # plt.legend()
    # plt.savefig(os.path.join(OUT_DIR, 'solutions_edges_' +
    #                          now + '.png'), bbox_inches="tight")
    # # plt.show()
    # plt.clf()

    ratios = []
    for i in range(len(greedy_solutions)):
        ratios.append(greedy_solutions[i]/edges_numbers[i])

    plt.title(
        "Ratio of the greedy algorithm duration / number of edges")
    plt_values = pd.DataFrame(
        {'edges': edges_numbers, 'ratio': ratios})
    plt.xlabel("Number of nodes")
    plt.ylabel("Ratio greedy/m")
    plt.plot('edges', 'ratio', data=plt_values,
             lw=2)
    plt.savefig(os.path.join(OUT_DIR, 'ratio_edges_' +
                             now + '.png'), bbox_inches="tight")
    # plt.show()
    plt.clf()


if __name__ == '__main__':
    main()
