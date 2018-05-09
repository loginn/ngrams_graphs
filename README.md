A library for ngram graph analysis of text inspired by the works of George Papadakis, George Giannakopoulos and Georgios Paliouras 

https://www.researchgate.net/profile/George_Papadakis2/publication/280329981_Graph_vs_Bag_Representation_Models_for_the_Topic_Classification_of_Web_documents/links/5746ba9008ae298602f9fb3f.pdf


Usage : 
```python
import ngram_graphs

docs = ['hello world', 'hell of a hello world', 'NLP rocks']


# Create a generator for bigram graphs
generator = ngram_graphs.Generator(n=2)

# Change n
generator.set_n(3)

# Generate the graphs
graphs = generator.generate_text_graphs(docs, weight=1.0)
```

To use word ngrams : 
```python
# Generate the graphs
graphs = generator.generate_text_graphs(docs, weight=1.0, token=True, sep=' ')
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