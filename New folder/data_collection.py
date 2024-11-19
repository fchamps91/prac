import pandas as pd
import networkx as nx

# Data collection form
data_collection_form = pd.DataFrame({
    'Node1': [1, 2, 3, 1, 4],
    'Node2': [2, 3, 4, 5, 5],
    'Weight': [0.5, 0.8, 0.2, 0.7, 0.9]
})
print("Data Collection Form:")
print(data_collection_form)

# One-mode dataset
one_mode_data = pd.DataFrame({
    'Node': [1, 2, 3, 4],
    'Attribute1': ['A', 'B', 'C', 'D'],
    'Attribute2': [10, 20, 15, 25]
})
print("\nOne-Mode Dataset:")
print(one_mode_data)

# Two-mode dataset
two_mode_data = pd.DataFrame({
    'Node1': [1, 2, 3, 1, 4],
    'Node2': ['A', 'B', 'C', 'D', 'A'],
    'Weight': [0.5, 0.8, 0.2, 0.7, 0.9]
})
print("\nTwo-Mode Dataset:")
print(two_mode_data)

# Creating a one-mode graph
G_one_mode = nx.from_pandas_edgelist(data_collection_form, 'Node1', 'Node2', ['Weight'], create_using=nx.Graph())
print("\nOne-Mode Graph:")
print(G_one_mode.edges(data=True))

# Creating a two-mode graph
B_one_mode = nx.from_pandas_edgelist(two_mode_data, 'Node1', 'Node2', ['Weight'], create_using=nx.Graph())
print("\nTwo-Mode Graph:")
print(B_one_mode.edges(data=True))

# Adjacency matrix for the one-mode graph
adjacency_matrix = nx.to_numpy_array(G_one_mode)
print("\nAdjacency Matrix:")
print(adjacency_matrix)