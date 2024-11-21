# Makenzy / Jeff Modifications

The basic workflow is to run the scripts below in the same order. The first one creates a named pickle file
and the other ones refer to it based on parameteres

# Network creation 
This one builds the network. Parameters are: 
- seed
- learning rate A
- forgetting time scale tau
- num neurons N

Example: 
`python dynamics/forgetting_create_connectivities.py 42 0.8 1.5 1000`

# Study forgetting and retrieval

This retrieves a specific memory, and finds the pickle file using the same conventions as above

There is one additional parameter, the first one, which is a pattern number.

Example:
`python dynamics/forgetting_retrieve_memory.py 42 1 0.8 1.5 1000`

# Plotting

This one plots the results from the memory one.

Example: 
` python Overlaps.py 42 0.8 1.5 1000`

# Original README contents

Code correspondiong to the preprint "Forgetting leads to chaos in attractor networks" in https://arxiv.org/abs/2112.00119 by U. Pereira-Obilinovic, J. Aljadeff, N. Brunel.
## dynamics

This folder contains the neccesary scripts and classes for the network simulations.

## MFT

This folder contains the neccesary scripts and classes for solving the corresponding mean field equations from 
the dynamical mean field theory.


## Plots

This folder contains the jupyter notebooks corresponding to figure 1 and 2 on the paper. If the jupyter notebooks for the rest of the figures are needed please contact me to the email below. 

## files
This folder contains the data and curves that are plotted on the directory plots.


Questions please contact me to: upo201@nyu.edu
