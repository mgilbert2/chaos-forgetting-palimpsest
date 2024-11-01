import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys

parameters_values = dict(
    seed=int(sys.argv[1]),  # random seed
    N=int(sys.argv[4]),  # number of neurons
    tau=float(sys.argv[3]),  # neuron timescale
    amp=float(sys.argv[2]),
)
A = str(round(parameters_values['amp'], 2))
N = str(int(parameters_values['N']/1000))
real = str(int(parameters_values['seed']))
tau = str(round(parameters_values['tau'], 2))
name = 'retrieval_N_' + N + 'K_seed_'+ real +'_tau_' + tau +'_A_'+ A + '_p_1.p'
print(name)

with open(name, 'rb') as f:
    results = pickle.load(f)

# overlaps shape is [time_steps, num_patterns])
overlaps = np.array(results['dynamics']['q_all'])  # All overlap values between the network’s state and stored memory patterns over time.
print(f"Shape of overlaps: {overlaps.shape}") 

# individual overlaps for each pattern
time_steps = overlaps.shape[0]
num_patterns = overlaps.shape[1]

# plt.figure(figsize=(12, 8))

# for pattern_idx in range(num_patterns):
#     plt.plot(range(time_steps), overlaps[:, pattern_idx], label=f'Pattern {pattern_idx + 1}', alpha=0.6)

# plt.xlabel('Time Steps')
# plt.ylabel('Overlap')
# plt.title('Overlap for All Patterns Over Time')
# plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1), ncol=2)
# plt.show()

# Mean and variance of overlaps for each pattern
mean_overlaps = overlaps.mean(axis=0)  # across time for each pattern
variance_overlaps = overlaps.var(axis=0)  

print(f"Mean overlaps for each pattern: {mean_overlaps}")
print(f"Variance of overlaps for each pattern: {variance_overlaps}")

# mean and variance for all patterns
fig, ax = plt.subplots(2, 1, figsize=(10, 8))

ax[0].bar(range(1, num_patterns + 1), mean_overlaps)
ax[0].set_title('Mean Overlap for Each Pattern')
ax[0].set_xlabel('Pattern Number')
ax[0].set_ylabel('Mean Overlap')

ax[1].bar(range(1, num_patterns + 1), variance_overlaps, color='orange')
ax[1].set_title('Variance of Overlap for Each Pattern')
ax[1].set_xlabel('Pattern Number')
ax[1].set_ylabel('Variance of Overlap')

plt.tight_layout()
plt.show()

df_overlaps = pd.DataFrame(overlaps, columns=[f'Pattern {i+1}' for i in range(overlaps.shape[1])])

# Column for Time Steps 
df_overlaps['Time Step'] = df_overlaps.index
df_overlaps = df_overlaps[['Time Step'] + [f'Pattern {i+1}' for i in range(overlaps.shape[1])]]

print(df_overlaps)
# df_overlaps.to_excel('overlaps_dataframe.xlsx', index=False)

overlaps = np.array(results['dynamics']['q_all']) 
print(f"Shape of overlaps: {overlaps.shape}") 

time_steps = overlaps.shape[0]
num_patterns = overlaps.shape[1]
df_overlaps = pd.DataFrame(overlaps, columns=[f'Pattern {i+1}' for i in range(overlaps.shape[1])])
df_overlaps['Time Step'] = df_overlaps.index
df_overlaps = df_overlaps[['Time Step'] + [f'Pattern {i+1}' for i in range(overlaps.shape[1])]]
first_five_patterns = df_overlaps.columns[1:6]  # Patterns 1 to 5
last_five_patterns = df_overlaps.columns[-5:]   # Last 5 patterns 

plt.figure(figsize=(12, 6))
for pattern in first_five_patterns:
    plt.plot(df_overlaps['Time Step'], df_overlaps[pattern], label=pattern, alpha=0.6)

plt.xlabel('Time Steps')
plt.ylabel('Overlap')
plt.title('Memory Overlap Over Time for Early Patterns (1-5)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
for pattern in last_five_patterns:
    plt.plot(df_overlaps['Time Step'], df_overlaps[pattern], label=pattern, alpha=0.6)

plt.xlabel('Time Steps')
plt.ylabel('Overlap')
plt.title('Memory Overlap Over Time for Late Patterns')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
