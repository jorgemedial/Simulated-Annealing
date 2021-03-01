import numpy as np
import networkx as nx
import numpy.random as rnd
import matplotlib.pyplot as plt
#Testing a rewiring function for graphs

def lap_to_adj(a):
    return np.diag(a)*np.eye(len(a))-a   

def draw_graph_lap(a):
    adj = lap_to_adj(a)
    G = nx.from_numpy_array(adj)
    nx.draw_spring(G)
    plt.show()

def erdos_renyi_laplacian(N = 24, k_mean = 3):
    #A Erdos Renyi graph is created with N nodes and mean_k 
    #adj matrix of a undirected graph
    L = int(N*k_mean/2)
    adj = np.zeros([N,N], dtype=int) 
    for _ in range(L):
        empty = False
        while not empty:
            i,j = rnd.randint(0,N,2)
            if adj[i,j]==0 and i !=j:
                empty = True
                adj[i,j] = adj[j,i] = 1
    a = sum(adj)*np.eye(N, dtype = int)-adj
    return a


#Algorithm of L preserving rewiring
def find_link(a, N = None): 
    #removes a link from the laplacian matrix a
    # a passes as reference
    #Returns nothing
    if N == None:
        N = len(a)
    link_found = False
    #Detects one link
    while not link_found:
        i, j = rnd.randint(0, N, 2)
        if a[i,j] == -1 and a[i,i] != 1 and a[j,j] != 1:
            link_found = True
    return [i,j]

def dewire(a, link):
    [i,j] = link
    a[i,i]-= 1
    a[i,j] = a[j,i] = 0
    a[j,j]-= 1

def find_vacant(a, N = None):
    #adds a link to the laplacian matrix
    if N == None:
        N = len(a)
    vacant_found = False
    while not vacant_found:
        i, j = rnd.randint(0, N, 2)
        if a[i,j] == 0 and i != j:
            vacant_found = True
    return [i,j]

def rewire(a, vacant):
    [i, j] = vacant
    a[i,i]+=1
    a[j,j]+=1
    a[i,j] = a[j,i] = -1

def change_network(a, steps = 1, N = None):
    links_dewired = []
    vacants_rewired = []
    for _ in range(steps):
        link = find_link(a, N)
        dewire(a, link)
        links_dewired.append(link)

        vacant = find_vacant(a, N)
        rewire(a, vacant)
        vacants_rewired.append(vacant)
    
    return links_dewired, vacants_rewired

def redo_network(a, dewired_links, rewired_vacants):
    for link in dewired_links:
        rewire(a, link)
    
    for vacant in rewired_vacants:
        dewire(a, vacant)

def metropolis_step(a, T, Q1, N, n_changes = 1, q = -3):
    dewired_links, rewired_vacants = change_network(a, steps=n_changes, N = N)
    Q2 = eigenratio(a)
    inc_Q = Q2-Q1
    if inc_Q<0:
        p = 1
    elif T == 0:
        p = 0
    elif q == 0:
        p = min(1, np.exp(-inc_Q/T))
    else:
        p = min(1, (1-(1-q)*inc_Q/T)**(1/(1-q)))
    if p < np.random.rand():
        redo_network(a, dewired_links, rewired_vacants)
        Q2 = Q1
    return Q2

def simulated_annealing(a, n_cooldowns, mh_steps,  
                        cooldown_rate = 0.9, q = 0, n_changes = 1):
    N = len(a)
    Q1 = eigenratio(a)
    #Calculate initial T
    T = -np.infty
    Q1 = eigenratio(a)
    for _ in range(N):
        _, _ = change_network(a, steps = 1, N =N)
        Q2 = eigenratio(a)
        inc_Q = Q2-Q1
        T = T if inc_Q < T else inc_Q
        Q1 = Q2
    

    #Calculate 
    for _ in range(n_cooldowns):
        steps = 0
        while steps < mh_steps:
            Q1 = metropolis_step(a, T, Q1, N, n_changes = n_changes, q = q)
            steps+=1
        T *= cooldown_rate

def experiment(N=24, k = 3, n_exp = 300, n_cool = 100, mh_steps = None, T = 10, cr = 0.9):
    if mh_steps == None:
        mh_steps = 100*N
    eigen = np.infty
    for exp in range(n_exp):
        a = erdos_renyi_laplacian(N, k)
        simulated_annealing(a, n_cooldowns=n_cool, mh_steps= mh_steps, cooldown_rate= 0.9)
        if eigenratio(a)<eigen:
            eigen = eigenratio(a)
            save = a.copy()
        print(exp)
        print(eigenratio(a))
        print(eigen)
    return save



    
def eigenratio(a):
    spectra = np.linalg.eigh(a)[0] #returns spectrum of hermitian matrix
    N = len(spectra)
    l_max = spectra[-1]
    l_min = 0
    i = 0
    while l_min < 1e-10 and i<N:
        i+=1
        l_min = spectra[i]
        
    return l_max/l_min if i==1 else np.infty

