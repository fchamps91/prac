# With Weight
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Define the weighted graph
edges = [
    ('A', 'B', 4),
    ('A', 'C', 2),
    ('B', 'C', 5),
    ('B', 'D', 10),
    ('C', 'D', 3)
]

# Create a graph object
G = nx.DiGraph()  # Directed graph to show direction of edges

# Add edges with weights
G.add_weighted_edges_from(edges)

# Compute adjacency matrix
adj_matrix = nx.to_numpy_array(G, weight='weight')

# Print adjacency matrix
print("Weighted Adjacency Matrix:")
print(adj_matrix)

# Draw the graph with edge weights
plt.figure(figsize=(10, 7))
pos = nx.spring_layout(G)  # Positions for all nodes

# Draw nodes and edges
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue',
        font_size=15, font_weight='bold', edge_color='gray')

# Draw edge labels (weights)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

plt.title('Weighted Graph')
plt.show()


