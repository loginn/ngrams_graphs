from igraph import Graph


def find_node_name(graph, node_idx):
    return graph.vs[node_idx]["name"]


class IGraphTextGraph(Graph):
    def __init__(self):
        super().__init__()

    @staticmethod
    def __calc_new_weight(s_edge, weight, learning_factor) -> float:
        return s_edge["weight"] + ((weight - s_edge["weight"]) * learning_factor)

    def __add_unknown_vertices(self, other):
        for vertex in other.vs:
            if vertex["name"] not in self.vs["name"]:
                self.add_vertex(name=vertex["name"])

    def __add_unknown_edge(self, other, o_edge, learning_factor):
        source = find_node_name(other, o_edge.source)
        target = find_node_name(other, o_edge.target)
        self.add_edge(source, target, weight=o_edge["weight"] * learning_factor, name=source + ' ' + target)

    def __update_edges(self, other: 'IGraphTextGraph', learning_factor: float):
        for o_edge in other.es:
            s_edge = next(iter([e for e in self.es if e["name"] == o_edge["name"]]), None)
            if s_edge is not None:
                s_edge["weight"] = self.__calc_new_weight(s_edge, o_edge["weight"], learning_factor)
            else:
                self.__add_unknown_edge(other, o_edge, learning_factor)
        for s_edge in self.es:
            if s_edge["name"] not in other.es["name"]:
                s_edge["weight"] = self.__calc_new_weight(s_edge, 0, learning_factor)

    def update(self, other: 'IGraphTextGraph', learning_factor):
        self.__add_unknown_vertices(other)
        self.__update_edges(other, learning_factor)
