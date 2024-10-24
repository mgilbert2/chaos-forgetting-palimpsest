import pickle
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


file_path = 'C:/Users/Mak/Pereira-Obilinovic/chaos-forgetting-palimpsest/retrieval_N_0K_seed_42_tau_1.5_A_0.8_p_1.p'
with open(file_path, 'rb') as f:
    results = pickle.load(f)

# overlaps  shape is [time_steps, num_patterns])
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
df_overlaps.to_excel('overlaps_dataframe.xlsx', index=False)

plt.figure(figsize=(10, 8))
sns.heatmap(df_overlaps.iloc[:, 1:].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Between Overlaps of Different Patterns')
plt.show()

