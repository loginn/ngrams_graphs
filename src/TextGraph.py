from igraph import Graph

from src.utils import find_node_name


class TextGraph(Graph):
    def __init__(self):
        super().__init__()

    @staticmethod
    def __calc_new_weight(s_edge, o_edge, learning_factor) -> float:
        return s_edge["weight"] + ((o_edge["weight"] - s_edge["weight"]) * learning_factor)

    def __add_unknown_vertices(self, other):
        for vertex in other.vs:
            if vertex["name"] not in self.vs["name"]:
                self.add_vertex(name=vertex["name"])

    def __add_unknown_edge(self, other, o_edge, learning_factor):
        source = find_node_name(other, o_edge.source)
        target = find_node_name(other, o_edge.target)
        self.add_edge(source, target, weight=o_edge["weight"] * learning_factor, name=source+target)

    def __update_edges(self, other, learning_factor):
        for o_edge in other.es:
            s_edge = next(iter([e for e in self.es if e["name"] == o_edge["name"]]), None)
            if s_edge is not None:
                s_edge["weight"] = self.__calc_new_weight(s_edge, o_edge, learning_factor)
            else:
                self.__add_unknown_edge(other, o_edge, learning_factor)

    def update(self, other: 'TextGraph', learning_factor):
        self.__add_unknown_vertices(other)
        self.__update_edges(other, learning_factor)
