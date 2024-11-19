import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4)])

# Calculate various metrics
density = nx.density(G)
print(f"Density: {density}")

degree = dict(G.degree())
print(f"Degree: {degree}")

reciprocity = nx.reciprocity(G)
print(f"Reciprocity: {reciprocity}")

transitivity = nx.transitivity(G)
print(f"Transitivity: {transitivity}")

centralization = nx.degree_centrality(G)
print(f"Centralization: {centralization}")

clustering = nx.clustering(G)
print(f"Clustering: {clustering}")

# Draw the graph
nx.draw(G, with_labels=True)
plt.show()