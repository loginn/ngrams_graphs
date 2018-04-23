from src.Generator import Generator
from src.utils import generate_model_graph

n = 3
data = ['head of marketing', 'marketing manager', 'marketing marketing']

generator = Generator(n)

graphs = generator.generate_text_graphs(data, weight=1.0)

model = generate_model_graph(graphs, lr=0.5)

for e in model.es:
    print(e["weight"])
