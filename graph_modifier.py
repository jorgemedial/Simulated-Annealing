import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

M = np.array([[4, -1, -1, -1, -1],[-1,1,0,0,0],[-1, 0, 1, 0,0], [-1, 0, 0, 2, -1], [-1, 0, 0,-1, 2]])
G = nx.from_numpy_array(M)
nx.draw(G)