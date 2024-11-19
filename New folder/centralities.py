# example of Social Network Analysis (SNA) using centrality measures in Python:


import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add edges
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (4, 6), (5, 6)])

# Calculate centrality measures
degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
eigenvector_centrality = nx.eigenvector_centrality(G)
pagerank = nx.pagerank(G)

# Print centrality scores
print("Degree Centrality:")
for node, score in degree_centrality.items():
    print(f"Node {node}: {score}")

print("\nBetweenness Centrality:")
for node, score in betweenness_centrality.items():
    print(f"Node {node}: {score}")

print("\nCloseness Centrality:")
for node, score in closeness_centrality.items():
    print(f"Node {node}: {score}")

print("\nEigenvector Centrality:")
for node, score in eigenvector_centrality.items():
    print(f"Node {node}: {score}")

print("\nPagerank:")
for node, score in pagerank.items():
    print(f"Node {node}: {score}")


# Visualize the graph
nx.draw(G, with_labels=True)
plt.show()