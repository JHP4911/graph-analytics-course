import networkx as nx
import matplotlib.pyplot as plt


# Importing graphs from a file
G = nx.read_graphml('../../dataset/graph-schema/graph.graphml')

# Draw without arrows
nx.draw(G, arrows=False)
plt.show()
