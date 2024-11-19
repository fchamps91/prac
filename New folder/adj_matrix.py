# Without Weight

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Define the unweighted graph (remove weights)
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'C'),
    ('B', 'D'),
    ('C', 'D')
]

# Create a graph object
G = nx.DiGraph()  # Directed graph to show direction of edges

# Add edges without weights
G.add_edges_from(edges)

# Compute adjacency matrix (unweighted)
adj_matrix = nx.to_numpy_array(G)

# Print adjacency matrix
print("Unweighted Adjacency Matrix:")
print(adj_matrix)

# Draw the graph without weights
plt.figure(figsize=(10, 7))
pos = nx.spring_layout(G)  # Positions for all nodes

# Draw nodes and edges
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue',
        font_size=15, font_weight='bold', edge_color='gray')

# Optionally, if you want to show edge labels (just for clarity, they will be empty)
edge_labels = {edge: '' for edge in G.edges()}  # Create empty labels for edges
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

plt.title('Unweighted Graph')
plt.show()
