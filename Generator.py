from TextGraph import TextGraph
from utils import find_edge


class Generator:
    def __init__(self, n):
        self.n = n
        self.graphs = []

    def __get_ngrams(self, doc):
        return [doc[x:x + self.n:1] for x in range(len(doc) - self.n + 1)]

    def generate_text_graphs(self, documents, weight):
        for doc in documents:
            graph = TextGraph()
            ngrams = self.__get_ngrams(doc)
            for gram in ngrams:
                if gram not in [v["name"] for v in graph.vs]:
                    graph.add_vertex(name=gram)

            for n1, n2 in zip(ngrams, ngrams[1:]):
                e = find_edge(graph, n1, n2)
                if e:
                    e["weight"] += weight
                else:
                    graph.add_edge(n1, n2, name=n1 + n2, weight=weight)

            self.graphs.append(graph)
        return self.graphs
