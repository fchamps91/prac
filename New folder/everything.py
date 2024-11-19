import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def compute_graph_properties(graph):
    num_edges = graph.number_of_edges()
    num_nodes = graph.number_of_nodes()
    node_degrees = dict(graph.degree())
    min_degree = min(node_degrees.values())
    adj_list = dict(graph.adjacency())
    adj_matrix = nx.adjacency_matrix(graph).todense()

    return num_edges, num_nodes, node_degrees, min_degree, adj_list, adj_matrix

def matrix_to_graph(adj_matrix):
    # Convert the adjacency matrix to a numpy matrix
    np_matrix = np.array(adj_matrix)
    # Create a graph from the numpy adjacency matrix
    return nx.from_numpy_array(np_matrix)

def plot_graph(graph):
    pos = nx.spring_layout(graph)  # positions for all nodes
    plt.figure(figsize=(8, 6))
    nx.draw(graph, pos, with_labels=True, node_color='skyblue', node_size=700, edge_color='gray', font_size=15, font_weight='bold')
    plt.title("Graph Visualization")
    plt.show()

# Create a graph
B = nx.Graph()
B.add_edges_from([(1, 2), (3, 5), (2, 3), (4, 1), (2, 4)])

# Compute graph properties
no_of_edge, no_of_node, node_d, min_d, adjacency_list, adjacency_matrix = compute_graph_properties(B)

# Create a graph from the adjacency matrix
graph_from_matrix = matrix_to_graph(adjacency_matrix)

# Print the results
print("Number of Edges are:", no_of_edge)
print("Number of Nodes are:", no_of_node)
print("Degree of Graph are:", node_d)
print("Minimum degree of graph are:", min_d)
print("Adjacency list:", adjacency_list)
print("Adjacency matrix:\n", adjacency_matrix)

# Print the edges of the graph created from the adjacency matrix
print("Edges of the graph created from adjacency matrix:", list(graph_from_matrix.edges()))

# Plot the graph
plot_graph(graph_from_matrix)
