from src.Generator import Generator
from src.utils import generate_model_graph
from src.comparison import *

n = 2
data = ['head of marketing', 'marketing manager', 'marketing consultant', 'marketing']
test = ['marketing manager', 'market analysis', 'construction worker']

generator = Generator(n)

graphs = generator.generate_text_graphs(data)
test_graphs = generator.generate_text_graphs(test)

g1 = generate_model_graph(graphs)

for idx, g2 in enumerate(test_graphs):
    print(test[idx])
    print('\tsize similarity :\t\t\t\t', size_similarity(g1, g2))
    print('\tcontainment_similarity :\t\t', containment_similarity(g1, g2))
    print('\tvalue_similarity :\t\t\t\t', value_similarity(g1, g2))
    print('\tnormalized_value_similarity :\t', normalized_value_similarity(g1, g2))
