import networkx as nx
import matplotlib.pyplot as plt

# 1. Persons-by-Persons Network (One-Mode Network)
# Create a graph for the persons-by-persons network
G_persons = nx.Graph()

# Add edges based on the relationships
# A, B, C, D, E are people
relationships = [
    ('A', 'B'),  # A is friends with B
    ('A', 'C'),  # A is friends with C
    ('B', 'D'),  # B is friends with D
    ('C', 'E')   # C is friends with E
]
G_persons.add_edges_from(relationships)

# Draw the Persons-by-Persons network
plt.figure(figsize=(6, 6))
nx.draw(G_persons, with_labels=True, node_color='lightblue', node_size=3000,
        font_size=12, font_weight='bold', edge_color='gray')
plt.title("Persons-by-Persons Network (One-Mode Network)")
plt.axis('off')  # Hide axes
plt.show()






# 2. Committee Network (Two-Node Network)
# Create a graph for the committee network
G_committees = nx.Graph()

# Nodes representing people
people = ['A', 'B', 'C', 'D', 'E']
# Nodes representing committees
committees = ['C1', 'C2', 'C3']

# Add edges based on the committee memberships
# A is part of C1 and C2, B is part of C2, etc.
committee_memberships = [
    ('A', 'C1'),
    ('A', 'C2'),
    ('B', 'C2'),
    ('C', 'C1'),
    ('C', 'C3'),
    ('D', 'C3'),
    ('E', 'C2'),
    ('E', 'C3')
]
G_committees.add_edges_from(committee_memberships)

# Draw the Committee Network (Two-Node Network)
plt.figure(figsize=(8, 8))
# Draw people and committees with different node shapes
pos = nx.spring_layout(G_committees)  # Position nodes using spring layout
nx.draw_networkx_nodes(G_committees, pos, nodelist=people, node_color='lightgreen',
                        node_size=3000)
nx.draw_networkx_nodes(G_committees, pos, nodelist=committees, node_color='lightcoral',
                        node_size=3000)
nx.draw_networkx_edges(G_committees, pos, edge_color='gray')

# Draw labels
nx.draw_networkx_labels(G_committees, pos, font_size=12, font_weight='bold')

# Title and display
plt.title("Committee Network (Two-Node Network)")
plt.axis('off')  # Hide axes
plt.show()