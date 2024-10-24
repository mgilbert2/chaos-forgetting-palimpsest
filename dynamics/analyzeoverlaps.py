import matplotlib.pyplot as plt

# Assuming `sol['overlaps']` contains the overlap data over time
overlaps = sol['overlaps']

# Plot the overlap over time to visualize its stability
plt.plot(overlaps)
plt.title('Overlap Over Time')
plt.xlabel('Time Step')
plt.ylabel('Overlap')
plt.show()
