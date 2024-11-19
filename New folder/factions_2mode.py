import networkx as nx
import matplotlib.pyplot as plt

# Create a two-mode network
# Nodes of type 'person' and 'event'
people = ['Steve', 'Damon', 'Ana', 'Stephan']
events = ['Event1', 'Event2', 'Event3']

# Create an empty bipartite graph
B = nx.Graph()

# Add nodes for people (set the bipartite attribute to 0)
B.add_nodes_from(people, bipartite=0)

# Add nodes for events (set the bipartite attribute to 1)
B.add_nodes_from(events, bipartite=1)

# Add edges between people and events
edges = [
    ('Steve', 'Event1'),
    ('Steve', 'Event2'),
    ('Damon', 'Event1'),
    ('Ana', 'Event2'),
    ('Stephan', 'Event3'),
    ('Ana', 'Event3'),
]
B.add_edges_from(edges)

# Draw the two-mode network
def draw_bipartite_graph(B):
    pos = nx.bipartite_layout(B, nodes=people)
    nx.draw(B, pos, with_labels=True, node_color=['skyblue' if n in people else 'lightgreen' for n in B.nodes()])
    plt.title("Two-Mode Network")
    plt.show()

# Function to perform two-mode faction analysis
def two_mode_faction_analysis(B):
    # Create a one-mode projection for people
    people_projection = nx.bipartite.projected_graph(B, people)
    # Analyze the factions using connected components
    factions = list(nx.connected_components(people_projection))
    return factions

# Draw the bipartite graph
draw_bipartite_graph(B)

# Perform the faction analysis
factions = two_mode_faction_analysis(B)

# Display the results
print("Identified Factions:")
for i, faction in enumerate(factions, 1):
    print(f"Faction {i}: {faction}")