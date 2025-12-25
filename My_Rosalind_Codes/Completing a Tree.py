import networkx as nx
#import matplotlib.pyplot as plt
import pyperclip

file_path = input("Enter the file path: ")
file_path = file_path.replace('"', '')

G = nx.Graph()

with open(file_path, 'r') as file:
    lines = file.readlines()
    n = int(lines[0].strip())
    for i in range(1, len(lines)):
        node1, node2 = map(int, lines[i].strip().split())
        G.add_edge(node1, node2)
    for z in range(1, n + 1):
        G.add_node(z)

num_components = nx.number_connected_components(G)
print(f"The number of edges to add to connect all the components is: {num_components - 1}")
pyperclip.copy(num_components - 1)

#nx.draw(G, with_labels=True)
#plt.show()