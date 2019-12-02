import networkx as nx
import os
import numpy as np

OUT_DIR = os.path.join('data', 'random_graphs')


def generate_graphs(p=0.2, start=10, stop=200, nb=20):
    if not os.path.exists(OUT_DIR):
        os.mkdir(OUT_DIR)
    if not os.path.exists(os.path.join(OUT_DIR, 'gexf')):
        os.mkdir(os.path.join(OUT_DIR, 'gexf'))
    if not os.path.exists(os.path.join(OUT_DIR, 'clq')):
        os.mkdir(os.path.join(OUT_DIR, 'clq'))
    for n in np.linspace(start, stop, nb):
        n = int(n)
        g = nx.fast_gnp_random_graph(n, p)
        filename = 'Gnp' + str(n) + '_' + str(p).strip('.')
        nx.write_gexf(g, os.path.join(OUT_DIR, 'gexf', filename + '.gexf'))
        with open(os.path.join(OUT_DIR, 'clq', filename + '.clq'), "w") as f:
            # writes the header
            f.write("p EDGE {} {}\n".format(
                g.number_of_nodes(), g.number_of_edges()))
            # writes all edges
            for u, v in g.edges():
                f.write("e {} {}\n".format(u, v))


def main():
    generate_graphs()


if __name__ == '__main__':
    main()
