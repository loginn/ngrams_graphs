from unittest import TestCase

import ngram_graphs


class TestGraphs(TestCase):
    def setUp(self):
        n = 2
        self.data = ['head of marketing', 'marketing manager', 'marketing consultant', 'marketing']
        self.test = ['marketing manager', 'market analysis', 'construction worker']

        generator = ngram_graphs.Generator(n)

        self.data_graphs = generator.generate_text_graphs(self.data)
        self.test_graphs = generator.generate_text_graphs(self.test)

    def test_graph_sizes(self):
        self.assertEqual(len(self.data_graphs), 4)
        self.assertEqual(len(self.test_graphs), 3)

        self.assertEqual(len(self.data_graphs[0].vs), 16)
        self.assertEqual(len(self.data_graphs[0].es), 15)

    def test_comparisons(self):
        g1 = ngram_graphs.generate_model_graph(self.data_graphs)

        for idx, g2 in enumerate(self.test_graphs):
            print(self.test[idx])
            print('\tsize_similarity :\t\t\t\t', ngram_graphs.size_similarity(g1, g2))
            print('\tcontainment_similarity :\t\t', ngram_graphs.containment_similarity(g1, g2))
            print('\tvalue_similarity :\t\t\t\t', ngram_graphs.value_similarity(g1, g2))
            print('\tnormalized_value_similarity :\t', ngram_graphs.normalized_value_similarity(g1, g2))

