from setuptools import setup

setup(name='ngram_graphs',
      version='0.1.7',
      description='An igraph or networkx based ngram graph library for NLP',
      long_description="""Library for ngram graph comparison based on papers from George Giannakopoulos and Vangelis Karkaletsis. The library uses igraph to create directed and weighted graphs from documents and provides means to compare them using the distance metrics defined in 'Giannakopoulos, George & Karkaletsis, Vangelis. (2009). N-gram graphs: Representing documents and document sets in summary system evaluation. '""",
      url='https://github.com/loginn/ngrams_graphs',
      author='loginn',
      classifiers=[
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='ngrams graph NLP',
      author_email='vincent.kurta2@gmail.com',
      license='MIT',
      install_requires=['python-igraph', 'networkx'],
      packages=['ngram_graphs'],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'],
      )
