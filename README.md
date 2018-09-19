A library for ngram graph analysis of text inspired by the works of George Papadakis, George Giannakopoulos and Georgios Paliouras 

https://www.researchgate.net/profile/George_Papadakis2/publication/280329981_Graph_vs_Bag_Representation_Models_for_the_Topic_Classification_of_Web_documents/links/5746ba9008ae298602f9fb3f.pdf


Installation : 
`pip install ngram-graphs`

Usage : 
```python
import ngram_graphs

docs = ['hello world', 'hell of a hello world', 'NLP rocks']


# Create a generator for bigram graphs
# Kind can be either 'igraph' (default) or 'networkx'
generator = ngram_graphs.Generator(n=2, kind='networkx')

# Change n for trigrams
generator.set_n(3)

# Generate the graphs
# By default the generator will use character level ngrams
graphs = generator.generate_text_graphs(docs, weight=1.0)
```

Different ways to get ngrams : 
```python
# Generate the graphs
# Word ngrams using split() 
graphs = generator.generate_text_graphs(docs, weight=1.0, wordgram=True)

# Word ngrams using split(sep) with a single char separator
graphs = generator.generate_text_graphs(docs, weight=1.0, wordgram=True, sep=' ')

# ngrams using re.split(sep, doc) with a regular expression
graphs = generator.generate_text_graphs(docs, weight=1.0, sep='\W+')

# ngrams using a custom function. The function must take str as input and return List[str]
# The ngrams will be constructed from the returned list so the function must not construct the ngrams itself
graphs = generator.generate_text_graphs(docs, weight=1.0, sep=lambda x: x.split())
```

Compare the graphs :

```python
print("How similar are the graphs' sizes ?")
print("SS : {}".format(ngram_graphs.size_similarity(graphs[0], graphs[1])))
print("SS : {}".format(ngram_graphs.size_similarity(graphs[1], graphs[2])))
print()

print("How similar are the graphs' edges ?")
print("CS : {}".format(ngram_graphs.containment_similarity(graphs[0], graphs[1])))
print("CS : {}".format(ngram_graphs.containment_similarity(graphs[1], graphs[2])))
print()

print("How similar are the graphs' edges taking weighting in account ?")
print("VS : {}".format(ngram_graphs.value_similarity(graphs[0], graphs[1])))
print("VS : {}".format(ngram_graphs.value_similarity(graphs[1], graphs[2])))
print()

print("How similar are the graphs' edges taking weighting in account and factoring out size ?")
print("NVS : {}".format(ngram_graphs.normalized_value_similarity(graphs[0], graphs[1])))
print("NVS : {}".format(ngram_graphs.normalized_value_similarity(graphs[1], graphs[2])))
```

Output : 

```
How similar are the graphs' sizes ?
SS : 0.5294117647058824
SS : 0.4117647058823529

How similar are the graphs' edges ?
CS : 0.5294117647058824
CS : 0.0

How similar are the graphs' edges taking weighting in account ?
VS : 0.47058823529411764
VS : 0.0

How similar are the graphs' edges taking weighting in account and factoring out size ?
NVS : 0.8888888888888888
NVS : 0.0
```