from typing import List

from ngram_graphs.TextGraph import TextGraph
from ngram_graphs.utils import find_edge


class Generator:
    def __init__(self, n):
        self.n = n
        self.__validate_generator()

    def __validate_generator(self):
        if self.n < 1:
            raise ValueError(f'{self.n} is not a valid value for n')

    def __get_ngrams(self, doc: str):
        return [doc[x:x + self.n:1] for x in range(len(doc) - self.n + 1)]

    def __get_wordngrams(self, doc: str, sep: str):
        doc = doc.split(sep)
        return [doc[x:x + self.n:1] for x in range(len(doc) - self.n + 1)]

    def __generate_text_graph(self, doc: str, weight: float, token: bool, sep: str):
        graph = TextGraph()
        if token:
            ngrams = self.__get_wordngrams(doc, sep)
        else:
            ngrams = self.__get_ngrams(doc)
        for gram in ngrams:
            if gram not in [v["name"] for v in graph.vs]:
                graph.add_vertex(name=gram)

        for n1, n2 in zip(ngrams, ngrams[1:]):
            e = find_edge(graph, n1, n2)
            if e:
                e["weight"] += weight
            else:
                graph.add_edge(n1, n2, name=n1 + ' ' + n2, weight=weight)
        return graph

    def generate_text_graphs(self, documents: List[str], weight: float=1.0, token: bool=False, sep: str=' '):
        graphs = [self.generate_text_graphs(doc, weight, token, sep) for doc in documents]
        return graphs
