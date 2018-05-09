def size_similarity(g1, g2):
    s1 = len(g1.es)
    s2 = len(g2.es)

    if not s1 or not s2:
        return None

    return min(s1, s2) / max(s1, s2)


def containment_similarity(g1, g2):
    s1 = len(g1.es)
    s2 = len(g2.es)
    if not s1 or not s2:
        return None
    common_edges = [e for e in g1.es if e["name"] in g2.es["name"]]

    return len(common_edges) / max(s1, s2)


def value_ratio(e1, e2):
    w1 = e1["weight"]
    w2 = e2["weight"]

    return min(w1, w2) / max(w1, w2)


def value_similarity(g1, g2):
    s1 = len(g1.es)
    s2 = len(g2.es)

    common_edges = [(e1, e2) for e1 in g1.es for e2 in g2.es if e1["name"] == e2["name"]]

    return sum(value_ratio(e[0], e[1]) for e in common_edges) / max(s1, s2)


def normalized_value_similarity(g1, g2):
    s = size_similarity(g1, g2)
    v = value_similarity(g1, g2)
    if not s:
        return None
    return v / s
