A library for ngram graph analysis of text


Usage: 
```python
import ngram_graphs

docs = ['hello world', 'NLP rocks']

generator = ngram_graphs.Generator(n=2)
graphs = generator.generate_text_graphs(docs, weight=1.0)

print(ngram_graphs.normalized_value_similarity(graphs[0], graphs[1]))
print(ngram_graphs.value_similarity(graphs[0], graphs[1]))
print(ngram_graphs.containment_similarity(graphs[0], graphs[1]))
print(ngram_graphs.size_similarity(graphs[0], graphs[1]))
```