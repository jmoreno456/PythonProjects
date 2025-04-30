# Import libraries
import networkx as nx
import matplotlib.pyplot as plt
# Create an empty undirected graph
my_graph = nx.Graph()
# Define edges between users and movies they watched
edges = [
    ('U1', 'Inception'),
    ('U1', 'Avatar'),
    ('U2', 'Interstellar'),
    ('U2', 'The Matrix'),
    ('U3', 'Interstellar'),
    ('U3', 'Avengers'),
    ('U3', 'Titanic'),
    ('U4', 'Forrest Gump'),
    ('U4', 'Titanic'),
    ('U5', 'Inception'),
    ('U5', 'Interstellar'),
    ('U5', 'The Matrix')
]
# create subset of edges that represent users favorite movies
favorite_edges = [('U1', 'Inception'), ('U2', 'Interstellar'),
                  ('U3', 'Interstellar'), ('U4', 'Forrest Gump'),
                  ('U5', 'Inception')]
# add all edges to graph created earlier
my_graph.add_edges_from(edges)
# generate layout for nodes
pos = nx.spring_layout(my_graph)
# draw all movie user edges
nx.draw_networkx_edges(my_graph, pos, edgelist=edges, edge_color='blue', width=1)
# draw all favorite movie edges
nx.draw_networkx_edges(my_graph, pos, edgelist=favorite_edges, edge_color='green', width=1)

# draw nodes in red
nx.draw_networkx_nodes(my_graph, pos, node_color='red')
# label each node 
nx.draw_networkx_labels(my_graph, pos, font_size=8)
# show graph
plt.show()
# print the number of connections for each node created
print(dict(my_graph.degree()))
