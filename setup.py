from setuptools import setup

setup(name='ngram_graphs',
      version='0.1',
      description='An igraph based ngram graph library for NLP',
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
