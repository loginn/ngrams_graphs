from setuptools import setup

setup(name='ngram_graphs',
      version='0.1',
      description='An igraph based ngram graph library for NLP',
      url='https://github.com/loginn/ngrams_graphs',
      author='loginn',
      author_email='vincent.kurta2@gmail.com',
      license='MIT',
      install_requires=['python-igraph'],
      packages=['ngram_graphs'],
      zip_safe=False)
