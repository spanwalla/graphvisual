from pyvis.network import Network
from . import schemas


def visualize_graph_by_adjacency_list(graph: schemas.AdjacencyList) -> str:
    g = Network(directed=graph.directed, height='98vh')
    for node in graph.edges.keys():
        color = graph.colors.get(node, graph.default_color)
        label = graph.labels.get(node, str(node))
        g.add_node(node, label=label, color=color)

    for node, neighbors in graph.edges.items():
        for i in neighbors:
            g.add_edge(node, i)

    g.toggle_physics(graph.physics)
    g.set_edge_smooth("continuous")
    return g.generate_html()
