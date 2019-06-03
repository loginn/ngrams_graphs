from typing import Union

from ngram_graphs.TextGraph.IGraphTextGraph import IGraphTextGraph
from ngram_graphs.TextGraph.NetworkxTextGraph import NetworkxTextGraph


def size_similarity(g1: Union[IGraphTextGraph, NetworkxTextGraph], g2: Union[IGraphTextGraph, NetworkxTextGraph]):
    if isinstance(g1, IGraphTextGraph) and isinstance(g2, IGraphTextGraph):
        s1 = len(g1.es)
        s2 = len(g2.es)
    elif isinstance(g1, NetworkxTextGraph) and isinstance(g2, NetworkxTextGraph):
        s1 = len(g1.edges)
        s2 = len(g2.edges)
    else:
        raise TypeError(f'Invalid Graph types\ng1 is a {type(g1)} and g2 is a {type(g2)}')

    if not s1 or not s2:
        return None

    return min(s1, s2) / max(s1, s2)


def containment_similarity(g1: Union[IGraphTextGraph, NetworkxTextGraph], g2: Union[IGraphTextGraph, NetworkxTextGraph]):
    if isinstance(g1, IGraphTextGraph) and isinstance(g2, IGraphTextGraph):
        s1 = len(g1.es)
        s2 = len(g2.es)
        if not s1 or not s2:
            return None
        common_edges = [e for e in g1.es if e["name"] in g2.es["name"]]

        return len(common_edges) / max(s1, s2)
    elif isinstance(g1, NetworkxTextGraph) and isinstance(g2, NetworkxTextGraph):
        s1 = len(g1.edges)
        s2 = len(g2.edges)
        if not s1 or not s2:
            return None
        common_edges = [e for e in g1.edges if e in g2.edges]

        return len(common_edges) / max(s1, s2)
    else:
        raise TypeError(f'Invalid Graph types\ng1 is a {type(g1)} and g2 is a {type(g2)}')


def value_ratio(e1, e2):
    w1 = e1["weight"]
    w2 = e2["weight"]

    return min(w1, w2) / max(w1, w2)


def value_similarity(g1: Union[IGraphTextGraph, NetworkxTextGraph], g2: Union[IGraphTextGraph, NetworkxTextGraph]):
    if isinstance(g1, IGraphTextGraph) and isinstance(g2, IGraphTextGraph):
        s1 = len(g1.es)
        s2 = len(g2.es)
        common_edges = [(e1, e2) for e1 in g1.es for e2 in g2.es if e1["name"] == e2["name"]]

        return sum(value_ratio(e[0], e[1]) for e in common_edges) / max(s1, s2)

    elif isinstance(g1, NetworkxTextGraph) and isinstance(g2, NetworkxTextGraph):
        e1 = set(g1.edges)
        e2 = set(g2.edges)

        s1 = len(e1)
        s2 = len(e2)

        common_edges = e1 & e2
        common_edges = [(g1.get_edge_data(t[0], t[1]), g2.get_edge_data(t[0], t[1])) for t in common_edges]
        return sum(value_ratio(e[0], e[1]) for e in common_edges) / max(s1, s2)
    else:
        raise TypeError(f'Invalid Graph types\ng1 is a {type(g1)} and g2 is a {type(g2)}')


def normalized_value_similarity(g1: Union[IGraphTextGraph, NetworkxTextGraph], g2: Union[IGraphTextGraph, NetworkxTextGraph]):
    s = size_similarity(g1, g2)
    v = value_similarity(g1, g2)
    if not s:
        return None
    return v / s
