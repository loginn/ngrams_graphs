from setuptools import setup

setup(name='ngram_graphs',
      version='0.1.1',
      description='An igraph based ngram graph library for NLP',
      long_description="""  Library for ngram graph comparison based on papers from Ioannis Kontopoulos, 
                            George Giannakopoulos and Iraklis Varlamis. 
                            The library uses igraph to create directed and weighted graphs from documents and provides
                            means to compare them using the distance metrics defined in 'Kontopoulos, Ioannis & Giannakopoulos, George & Varlamis, Iraklis. (2017). Distributing N-Gram Graphs for Classification. 3-11. 10.1007/978-3-319-67162-8_1.'""",
      url='https://github.com/loginn/ngrams_graphs',
      author='loginn',
      classifiers=[
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='ngrams graph NLP',
      author_email='vincent.kurta2@gmail.com',
      license='MIT',
      install_requires=['python-igraph'],
      packages=['ngram_graphs'],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'],
      )
