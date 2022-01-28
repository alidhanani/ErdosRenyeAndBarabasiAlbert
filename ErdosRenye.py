import networkx
import math
import numpy as np
import scipy.stats as stats
from random import randrange

def erdos_renyi_graph(n, k):

    """Build the graph with n nodes and a average number of degree
    :param n: number of average node in the network
    :param pEdge: probability that there is an edge between any pair of nodes
    :returns: a network"""
			
    g = networkx.empty_graph(n)
    V = (k*n)/2
    # run through all the possible edges
    networkx.set_node_attributes(g, 0, "state")
    networkx.set_node_attributes(g, 0, "payoff")
    ne = 0
    for i in range(n):
        for j in range(int(V)):
            if g.has_edge(i, j) == False:
                g.add_edge(i, j, attr_dict = np.random.randint(0,high=1))
                ne += 1
    return g
G = erdos_renyi_graph_from_scratch(1000, 4)
