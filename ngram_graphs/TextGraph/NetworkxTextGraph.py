from networkx import DiGraph


def find_node_name(graph, name):
    try:
        return graph.nodes[name]
    except KeyError:
        return None


class NetworkxTextGraph(DiGraph):
    def __init__(self):
        super().__init__()

    @staticmethod
    def __calc_new_weight(s_edge, weight: float, learning_factor: float) -> float:
        return s_edge["weight"] + ((weight - s_edge["weight"]) * learning_factor)

    def __add_unknown_vertices(self, other):
        for vertex in other.nodes:
            self.add_node(vertex)

    def __add_unknown_edge(self, o_edge, learning_factor):
        source = o_edge[0]
        target = o_edge[1]
        self.add_edge(source, target, weight=o_edge[2]["weight"] * learning_factor, name=source + ' ' + target)

    def __update_edges(self, other: 'NetworkxTextGraph', learning_factor: float):
        for o_edge in other.edges(data=True):
            edge_tuple = (o_edge[0], o_edge[1])
            if self.has_edge(o_edge[0], o_edge[1]):
                self.edges()[edge_tuple].update({"weight": self.__calc_new_weight(self.edges()[edge_tuple], o_edge[2]["weight"], learning_factor)})
            else:
                self.__add_unknown_edge(o_edge, learning_factor)
        for s_edge in self.edges(data=True):
            edge_tuple = (s_edge[0], s_edge[1])
            if edge_tuple not in other.edges:
                self.edges[edge_tuple].update({"weight": self.__calc_new_weight(s_edge[2], 0, learning_factor)})

    def update(self, other: 'NetworkxTextGraph', learning_factor):
        self.__add_unknown_vertices(other)
        self.__update_edges(other, learning_factor)
