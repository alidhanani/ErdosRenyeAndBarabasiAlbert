import networkx
import math
import numpy as np
import scipy.stats as stats
from random import randrange

def barabasi_albert_graph_from_scratch(N): 	
	#This function is gonna take the number of nodes
	# return the network
    grap = networkx.empty_graph(4) 
    ne = 0 
    ArrayMax = [] 
    ArrayOfDegree = []
    grap.add_edge(4, 0, attr_dict = {'added': ne})
    grap.add_edge(4, 1, attr_dict = {'added': ne})
    grap.add_edge(4, 2, attr_dict = {'added': ne})
    grap.add_edge(4, 3, attr_dict = {'added': ne})
    for i in range(5,N):
        total = 0
        for j in range(i-1): 
            total += grap.degree[j]
        for j in range(i-1): 
            Pi = grap.degree[j]/total 
            ArrayMax.append(Pi)
            ArrayOfDegree.append(j)
        value1 = np.random.choice(ArrayOfDegree, 4,  replace=False, p=ArrayMax)
        for j in value1:    
            grap.add_edge(i, j, attr_dict = {'added': j})
        ArrayMax.clear()
        ArrayOfDegree.clear()
    networkx.set_node_attributes(grap, 0, "state")
    networkx.set_node_attributes(grap, 0, "payoff")
    return grap

b = barabasi_albert_graph_from_scratch(1000) 
