import networkx as nx
import matplotlib.pyplot as plt

my_graph = nx.Graph()

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

favorite_edges = [('U1', 'Inception'), ('U2', 'Interstellar'),
                  ('U3', 'Interstellar'), ('U4', 'Forrest Gump'),
                  ('U5', 'Inception')]

my_graph.add_edges_from(edges)
pos = nx.spring_layout(my_graph)

nx.draw_networkx_edges(my_graph, pos, edgelist=edges, edge_color='blue', width=1)
nx.draw_networkx_edges(my_graph, pos, edgelist=favorite_edges, edge_color='green', width=1)


nx.draw_networkx_nodes(my_graph, pos, node_color='red')
nx.draw_networkx_labels(my_graph, pos, font_size=8)

plt.show()

print(dict(my_graph.degree()))
