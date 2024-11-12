# Region 1 low learning and forgetting (fixed no retrieval)
python dynamics/forgetting_create_connectivities.py 42 0.2 1.0 1000
python dynamics/forgetting_retrieve_memory.py 42 1 1.0 0.2 1000
python Overlaps.py 42 0.2 1.0 1000 

# Region 2 medium learning rate 
python dynamics/forgetting_create_connectivities.py 42 0.8 1.0 1000
python dynamics/forgetting_retrieve_memory.py 42 1 1.0 0.8 1000
python Overlaps.py 42 0.8 1.0 1000

# Region 3 chaos with retrieval: medium learning rate and medium forgetting scale (a little more chaos)
python dynamics/forgetting_create_connectivities.py 42 1.5 0.8 1000
python dynamics/forgetting_retrieve_memory.py 42 1 0.8 1.5 1000
python Overlaps.py 42 1.5 0.8 1000


# Region 4 chaos no retrieval High learning rate and high forgetting scale not really chaos 
python dynamics/forgetting_create_connectivities.py 42 3.0 0.5 1000
python dynamics/forgetting_retrieve_memory.py 42 1 0.5 3.0 1000
python Overlaps.py 42 3.0 0.5 1000
