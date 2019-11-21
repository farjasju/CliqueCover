from collections import deque
import sys


class Graph(object):
    def __init__(self, adjmat):
        self.n = len(adjmat)
        self.adjmat = adjmat
        self.degree = [sum(row) for row in self.adjmat]

    def sort_by_degree(self):
        v_and_deg = sorted(zip(range(self.n), self.degree))
        # v_and_deg.sort(key=lambda x: x[1], reverse=True)
        vv = [x[0] for x in v_and_deg]
        self.adjmat = [[self.adjmat[v][w] for v in vv] for w in vv]

    def show(self):
        print(self.adjmat)


def read_instance(lines):
    lines = [line.strip().split()
             for line in lines if line.strip().split() != []]
    p_line = [line for line in lines if line[0] == 'p'][0]
    e_lines = [line for line in lines if line[0] == 'e']
    n = int(p_line[2])
    print("Number of vertices:"), n
    print("Number of edges:"), len(e_lines)
    adjmat = [[0] * n for _ in range(n)]
    for e in e_lines:
        v, w = int(e[1])-1, int(e[2])-1
        if v == w:
            print("Loop detected"), v
        if adjmat[v][w]:
            print("Duplicate edge"), v, w
        adjmat[v][w] = adjmat[w][v] = 1
    print("Finished reading instance.")
    return Graph(adjmat)


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        g = read_instance([line for line in f.readlines()])
    if len(sys.argv) < 3:
        g.sort_by_degree()
    g.show()
