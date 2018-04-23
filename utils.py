from typing import List


def find_node_name(graph, node_idx):
    return graph.vs[node_idx]["name"]


def find_node(graph, node_idx):
    return graph.vs[node_idx]


def find_edge(graph, source, target):
    for edge in graph.es:
        if (source, target) == (find_node_name(graph, edge.source), find_node_name(graph, edge.target)):
            return edge
    return None


def generate_model_graph(graphs: List, lr: float=0.5):
    model = graphs[0]
    for graph in graphs[1:]:
        model.update(graph, lr)
    return model
