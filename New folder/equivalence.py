import networkx as nx
import matplotlib.pyplot as plt

# Create a sample graph
edges = [
    (1, 2), (1, 3), (2, 4), (2, 5),
    (3, 6), (3, 7), (4, 8), (5, 8),
    (6, 8), (7, 8)
]
G = nx.Graph(edges)

# Function to find structural equivalence
def find_structural_equivalence(G):
    equivalence_classes = []
    for node in G.nodes():
        neighbors = set(G.neighbors(node))
        for eq_class in equivalence_classes:
            if neighbors == eq_class[0]:
                eq_class.append(node)
                break
        else:
            equivalence_classes.append([neighbors, node])
    return equivalence_classes

# Function to find automorphic equivalence
def find_automorphic_equivalence(G):
    equivalence_classes = []
    for node in G.nodes():
        degree_sequence = sorted([G.degree(neighbor) for neighbor in G.neighbors(node)])
        for eq_class in equivalence_classes:
            if degree_sequence == eq_class[0]:
                eq_class.append(node)
                break
        else:
            equivalence_classes.append([degree_sequence, node])
    return equivalence_classes

# Function to find regular equivalence
def find_regular_equivalence(G):
    equivalence_classes = []
    for node in G.nodes():
        connections = frozenset(G.neighbors(node))
        for eq_class in equivalence_classes:
            if connections == eq_class[0]:
                eq_class.append(node)
                break
        else:
            equivalence_classes.append([connections, node])
    return equivalence_classes

# Calculate equivalences
structural_eq_classes = find_structural_equivalence(G)
automorphic_eq_classes = find_automorphic_equivalence(G)
regular_eq_classes = find_regular_equivalence(G)

# Display equivalence classes
print("Structural Equivalence Classes:")
for eq_class in structural_eq_classes:
    print(eq_class[1:])

print("\nAutomorphic Equivalence Classes:")
for eq_class in automorphic_eq_classes:
    print(eq_class[1:])

print("\nRegular Equivalence Classes:")
for eq_class in regular_eq_classes:
    print(eq_class[1:])

# Draw the network
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, width=2)
plt.title("Social Network")
plt.axis('off')
plt.show()