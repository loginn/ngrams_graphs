import re
from typing import List, Union, Callable

from ngram_graphs.TextGraph.IGraphTextGraph import IGraphTextGraph
from ngram_graphs.TextGraph.NetworkxTextGraph import NetworkxTextGraph
from ngram_graphs.utils import find_edge


class Generator:
    def __init__(self, n: int, kind: str = 'igraph'):
        self.n: int = n
        self.kind: str = kind
        self.__validate_generator()

    def __validate_generator(self):
        if self.n < 1:
            raise ValueError(f'{self.n} is not a valid value for n')
        if self.kind not in ['igraph', 'networkx']:
            raise ValueError(f'{self.kind} isn\'t a supported graph library. Please use "igraph" or "networkx"')

    def __get_chargrams(self, doc: str):
        return [doc[x:x + self.n:1] for x in range(len(doc) - self.n + 1)]

    def __get_regexngrams(self, doc: str, pattern: str):
        try:
            pattern = re.compile(pattern)
            doc = pattern.split(doc)
        except re.error as e:
            print(f"Error with regex '{pattern}'")
            raise re.error(e)
        grams = [doc[x:x + self.n:1] for x in range(len(doc) - self.n + 1)]
        return ['_'.join(g) for g in grams]

    def __get_wordngrams(self, doc: str, sep: str):
        if not sep:
            doc = doc.split()
        elif len(sep) == 1:
            doc = doc.split(sep)

        wordgrams = [doc[x:x + self.n:1] for x in range(len(doc) - self.n + 1)]
        return ['_'.join(wg) for wg in wordgrams]

    def __run_custom_function(self, doc: str, f: Callable[[str], List[str]]):
        return f(doc)

    def __generate_igraph(self, ngrams: List, weight: float):
        graph = IGraphTextGraph()
        for gram in ngrams:
            if gram not in [v["name"] for v in graph.vs]:
                graph.add_vertex(name=gram)

        for n1, n2 in zip(ngrams, ngrams[1:]):
            e = find_edge(graph, n1, n2)
            if e:
                e["weight"] += weight
            else:
                graph.add_edge(n1, n2, name=f'{n1} {n2}', weight=weight)
        return graph

    def __generate_networkx(self, ngrams: List, weight: float):
        graph = NetworkxTextGraph()
        for gram in ngrams:
            if gram not in graph.nodes:
                graph.add_node(gram)

        for n1, n2 in zip(ngrams, ngrams[1:]):
            e = find_edge(graph, n1, n2)
            if e:
                e["weight"] += weight
            else:
                graph.add_edge(n1, n2, name=f'{n1} {n2}', weight=weight)
        return graph

    def __generate_graph(self, ngrams: List, weight: float):
        if self.kind == 'igraph':
            return self.__generate_igraph(ngrams, weight)
        elif self.kind == 'networkx':
            return self.__generate_networkx(ngrams, weight)

    def __generate_text_graph(self, doc: str, weight: float, token: bool, sep: str):
        if token:
            graph = self.__generate_graph(self.__get_wordngrams(doc, sep), weight)
        elif isinstance(sep, str):
            graph = self.__generate_graph(self.__get_regexngrams(doc, sep), weight)
        elif isinstance(sep, Callable):
            graph = self.__generate_graph(self.__run_custom_function(doc, sep), weight)
        else:
            graph = self.__generate_graph(self.__get_chargrams(doc), weight)
        return graph

    def generate_text_graphs(self, documents: List[str], weight: float=1.0, wordgram: bool=False, sep: Union[str, Callable[[str], List[str]]]=None):
        graphs = [self.__generate_text_graph(doc, weight, wordgram, sep) for doc in documents]
        graphs = [g for g in graphs if len(g.es) > 0]
        return graphs

    def set_n(self, n):
        self.n = n
        self.__validate_generator()
