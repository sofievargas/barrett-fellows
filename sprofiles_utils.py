import networkx as nx
import triad_utils
import numpy as np
import scipy.sparse as sp
import matplotlib.pyplot as plt
import random as rn
import math

#format the csv into a list
def format_csv(raw_data):
    with open(raw_data, 'r') as file:
        lines = file.readlines()
    l = []
    for line in lines:
        if "TIME" in line:
            continue
        line = line[line.index(".0,")+3:]
        n1 = [int(x) for x in line.strip().split(",")]
        l.append(n1)
    return l

#convert a row entry into a matrix  
def convert_to_matrix(m):
    dimension = math.ceil(math.sqrt(len(m)))
    padded_data = m + [0]*dimension
    reshaped_data = np.array(padded_data).reshape(dimension,dimension)
    G = nx.from_numpy_array(reshaped_data,create_using=nx.DiGraph)
    G.edges(data=True)
    return G

#reformat the networkX triad census
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

def create_profile(network, step, file_name):
    list_of_matrices = format_csv(network)
    list_of_matrices = list_of_matrices[0:len(list_of_matrices):step]
    censuses = []
    sps = []
    for m in list_of_matrices:
        G = convert_to_matrix(m)
        census = convert_to_regular_triads(nx.triadic_census(G))
        censuses.append(census)
        significance_profile = triad_utils.triad_significance_profile(census,nx.adjacency_matrix(G).toarray(), 100,400)
        sps.append(significance_profile)
        #make the file name corresponding to the network, write significance profile to a text file
        with open(file_name + ".txt", "w") as file:
            string_profile = np.array(significance_profile).astype(str)
            file.write(" ".join(string_profile) + "\n")
    print("file successfully created")
    return censuses, sps

