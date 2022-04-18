# Wrapper for networkx's DiGraph.
import networkx as nx
import matplotlib.pyplot as plt


class Digraph:

    def __init__(self):

        self.digraph = nx.DiGraph()

    def addNodes(self, nodes):
        self.digraph.add_nodes_from(nodes)

    def addDirectedEdge(self, a, b, **kwargs):
        self.digraph.add_edge(a,b, **kwargs)


    def visualize(self):
        color_map = ['red' if node[0] is 'm' else 'green' for node in self.digraph]

        nx.draw_networkx(self.digraph,  with_labels=True, node_color=color_map)
        plt.show()

# Driver code
if __name__ == '__main__':
    G = Digraph()
    G.digraph.add_nodes_from(['m0','m1','m2','m3','m4'])
    G.digraph.add_nodes_from(['w0','w1','w2','w3','w4'])

    G.addDirectedEdge('w0', 'm2')
    color_map = ['red' if node[0] is 'm' else 'green' for node in G.digraph]

    # G.addDirectedEdge(1, 2)
    # G.addDirectedEdge(1, 3)
    # G.addDirectedEdge(5, 3)
    # G.addDirectedEdge(3, 4)
    # G.addDirectedEdge(1, 0)
    nx.draw(G.digraph, with_labels=True, node_color=color_map)
    print(G.digraph.nodes)
    plt.show()
    G = nx.complete_graph(5)
    nx.draw(G)