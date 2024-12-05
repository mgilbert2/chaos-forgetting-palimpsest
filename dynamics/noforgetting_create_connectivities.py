import numpy as np
import pickle
import time
from classes.network_dynamics import *
import sys
import os

tag = int(sys.argv[1])# tag realization/seed
amp = float(sys.argv[2])
tau_pal =  float(sys.argv[3])
N = int(sys.argv[4])
alpha = float(sys.argv[5])  # Memory load (alpha)

parameters_values = dict(
    seed=tag,  # random seed
    N=N,  # number of neurons
    tau=20.,  # neuron timescale
    tau_palimpsest=tau_pal,  # forgetting timescale
    n_tau_palimpsest=6,  # number of tau forgetting (practically infinity)
    lr_data=False,
    amp=amp,
    qf=0.5,
    bf=1e6,
    bg=1e6,
    xf=0,
    xg=0,
    r_max=2.,
    q_tanh=0.5,
    beta=1,
    h0=0,
    which_tf='tanh',
    dt=0.5,  # time step
    T=2500,  # simulation time
    indexes_neurons=np.array([0]),  # neurons to save dynamics
    p=10  # MANUALLY SET NUMBER OF PATTERNS HERE
)

# Calculate connectivity scale (K) and patterns (p)
K = int(2 * np.log(parameters_values['N']))
p = int(alpha * K)  # Number of patterns
parameters_values['p'] = p
path = 'C:/Users/Mak/Pereira-Obilinovic/chaos-forgetting-palimpsest/'

A = str(round(parameters_values["amp"], 2))
alpha_str = str(round(alpha, 2))
name = f'matrix_N_{N}K_seed_{tag}_alpha_{alpha_str}_A_{A}.p'

# A = str(round(parameters_values['amp'], 2))
# N = str(int(parameters_values['N']/1000))
# real = str(int(parameters_values['seed']))
# tau = str(round(parameters_values['tau_palimpsest'], 2)) #time forgetting
# name = 'matrix_N_' + N + 'K_seed_'+ real +'_tau_' + tau +'_A_'+ A + '.p'
# if path == '':
#     pass
# else:
#     if not os.path.exists(path):
#         os.makedirs(path)
# #building connectivity
# conn = ConnectivityMatrix(parameters_values)
# conn.connectivity_generalized_hebbian()
# pickle.dump(conn, open(path+name, 'wb'), protocol=4)
conn = ConnectivityMatrix(parameters_values)
conn.connectivity_generalized_hebbian()
pickle.dump(conn, open(path + name, 'wb'), protocol=4)
print(f"Connectivity matrix saved as {name} with alpha={alpha}, p={p}, K={K}, A={amp}")
