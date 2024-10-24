# Seed, learning rate, forgetting scale, num neurons
python dynamics/forgetting_create_connectivities.py 42 0.8 1.5 100

# Seed, pattern number to retrieve, learning rate, forgetting scale, num neurons
python dynamics/forgetting_retrieve_memory.py 42 1 1.5 0.8 100