from ngram_graphs.TextGraph.IGraphTextGraph import IGraphTextGraph
from ngram_graphs.TextGraph.NetworkxTextGraph import NetworkxTextGraph


def size_similarity(g1, g2):
    if isinstance(g1, IGraphTextGraph) and isinstance(g2, IGraphTextGraph):
        s1 = len(g1.es)
        s2 = len(g2.es)
    elif isinstance(g1, NetworkxTextGraph) and isinstance(g2, NetworkxTextGraph):
        s1 = len(g1.edges)
        s2 = len(g2.edges)
    else:
        raise TypeError('Invalid Graph types')

    if not s1 or not s2:
        return None

    return min(s1, s2) / max(s1, s2)


def containment_similarity(g1, g2):
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
        raise TypeError('Invalid Graph types')


def value_ratio(e1, e2):
    w1 = e1["weight"]
    w2 = e2["weight"]

    return min(w1, w2) / max(w1, w2)


def value_similarity(g1, g2):
    if isinstance(g1, IGraphTextGraph) and isinstance(g2, IGraphTextGraph):
        s1 = len(g1.es)
        s2 = len(g2.es)
        common_edges = [(e1, e2) for e1 in g1.es for e2 in g2.es if e1["name"] == e2["name"]]

        return sum(value_ratio(e[0], e[1]) for e in common_edges) / max(s1, s2)

    elif isinstance(g1, NetworkxTextGraph) and isinstance(g2, NetworkxTextGraph):
        s1 = len(g1.edges)
        s2 = len(g2.edges)

        common_edges = [(e1, e2) for e1 in g1.edges(data=True) for e2 in g2.edges(data=True) if e1[2]['name'] == e2[2]['name']]
        return sum(value_ratio(e[0][2], e[1][2]) for e in common_edges) / max(s1, s2)
    else:
        raise TypeError('Invalid Graph types')


def normalized_value_similarity(g1, g2):
    s = size_similarity(g1, g2)
    v = value_similarity(g1, g2)
    if not s:
        return None
    return v / s
