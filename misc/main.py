import networkx as nx
import triad_utils
import numpy as np
import scipy.sparse as sp
import matplotlib.pyplot as plt
import methods
import random as rn

raw_data = "congress.edgelist"
with open(raw_data, 'r') as file:
    lines = file.readlines()

l = []
for line in lines:
    n1, n2 = line.strip().split(" ")[0:2]
    l.append((n1, n2))

def convert_to_regular_triads(networkx_triads):
    census = []
    census.append(networkx_triads['021D'])
    census.append(networkx_triads['021U'])
    census.append(networkx_triads['021C'])
    census.append(networkx_triads['111D'])
    census.append(networkx_triads['111U'])
    census.append(networkx_triads['201'])
    census.append(networkx_triads['030T'])
    census.append(networkx_triads['030C'])
    census.append(networkx_triads['120D'])
    census.append(networkx_triads['120U'])
    census.append(networkx_triads['120C'])
    census.append(networkx_triads['210'])
    census.append(networkx_triads['300'])
    return census


data = nx.DiGraph(l)
#print(list(data.nodes))
census = convert_to_regular_triads(nx.triadic_census(data))
print(nx.triadic_census(data))
for c in nx.triadic_census(data):\
    print("CENSUS: ", c, " ", nx.triadic_census(data)[c])
    
#print(methods.triad_census(list(data.nodes), list(data.edges)))data_matrix = nx.adjacency_matrix(data)
data_matrix = nx.adjacency_matrix(data)[3:][3:]
data_matrix = data_matrix.toarray()
significance_profile = triad_utils.triad_significance_profile(census, data_matrix, 100,400)
profile_plot = plt.plot(significance_profile, "o-")
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
image = plt.savefig("image.png")

"""data_matrix = nx.adjacency_matrix(data)
data_matrix = data_matrix.toarray()

print(triad_utils.triad_census(data_matrix))
edge_randoms = len(triad_utils.edge_list(data_matrix))*10
print(edge_randoms)
print(triad_utils.triad_significance_profile(data_matrix,10,4))
significance_profile = triad_utils.triad_significance_profile(data_matrix,10,4)
profile_plot = plt.plot(significance_profile)
image = plt.savefig("image.png", profile_plot)

#creates network with nodes and edges"""

"""
#find triad U21D
count_1, message_1 = methods.triad_1(nodes, edges)
print(count_1)
#print(message_1)
#b -> a <- c


count_2, message_2 = methods.triad_2(nodes, edges)
print(count_2)
#print(message_2)
#b <- a -> c

count_3, message_3 = methods.triad_3(nodes, edges)
print(count_3)
#print(message_3)

count_4, message_4 = methods.triad_4(nodes, edges)
print(count_4)

count_5, message_5 = methods.triad_5(nodes, edges)
print(count_5)
"""