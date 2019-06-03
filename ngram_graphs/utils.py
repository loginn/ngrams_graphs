from copy import copy
from typing import List, Union

from ngram_graphs.TextGraph.IGraphTextGraph import IGraphTextGraph, find_node_name
from ngram_graphs.TextGraph.NetworkxTextGraph import NetworkxTextGraph


def find_node(graph, node_idx):
    return graph.vs[node_idx]


def find_edge(graph, source, target):
    if isinstance(graph, IGraphTextGraph):
        for edge in graph.es:
            if (source, target) == (find_node_name(graph, edge.source), find_node_name(graph, edge.target)):
                return edge
        return None
    elif isinstance(graph, NetworkxTextGraph):
        if graph.has_edge(source, target):
            return graph.edges[source, target]
        return None


def generate_model_graph(graphs: List, lr: float = 0.5) -> Union[IGraphTextGraph, NetworkxTextGraph]:
    if not graphs:
        raise IndexError('Empty list of graph')
    model = copy(graphs[0])
    for graph in graphs[1:]:
        model.update(graph, lr)
    return model
