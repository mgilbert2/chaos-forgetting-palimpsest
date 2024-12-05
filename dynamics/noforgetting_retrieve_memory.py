import numpy as np
import pickle
import sys
import os
from classes.nonetwork_dynamics import *

# Parse command-line arguments
tag = int(sys.argv[1])  # Seed
p = int(sys.argv[2])  # Pattern number to retrieve
amp = float(sys.argv[3])  # Learning gain (A)
N = int(sys.argv[4])  # Number of neurons
alpha = float(sys.argv[5])  # Memory load (alpha)

# Parameters
parameters_values = dict(
    seed=tag,
    N=N,
    tau=20.0,  # Neuron timescale
    tau_palimpsest=np.inf,  # Disable forgetting
    n_tau_palimpsest=6,  # Ignored in no-forgetting
    lr_data=False,
    amp=amp,
    qf=0.5,
    bf=1e6,
    bg=1e6,
    xf=0,
    xg=0,
    r_max=2.0,
    q_tanh=0.5,
    beta=1.0,
    h0=0.0,
    which_tf="tanh",
    dt=0.5,
    T=4000,
    indexes_neurons=np.array([range(100)])  # Neurons to save
)

# Load connectivity matrix
K = int(2 * np.log(parameters_values['N']))
filename = f"matrix_N_{N}_seed_{tag}_alpha_{alpha:.3f}_A_{amp:.2f}.p"
conn = pickle.load(open(os.path.join('./', filename), 'rb'))

# Simulate retrieval
ind = (p - 1, p)  # Pattern range for retrieval
dyn = NetworkDynamics(parameters_values, conn)

# Initialize dynamics with the selected pattern
u_init = conn.myLR.g(conn.patterns[ind[1] - 1])

# Simulate
sol = dyn.dynamics(u_init, ind)

# Save results
results_filename = f"retrieval_N_{N}_seed_{tag}_alpha_{alpha:.3f}_A_{amp:.2f}_p_{p}.p"
pickle.dump({'parameters': parameters_values, 'dynamics': sol}, open(os.path.join('./', results_filename), 'wb'))
print(f"Simulation results saved as {results_filename}")
