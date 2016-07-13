#!/usr/bin/env python
from setuptools import setup

setup(
    name='robograph',
    version='0.0.3',
    description='A graph-oriented algorithmic engine',
    author='Claudio Sparpaglione (@csparpa)',
    author_email='csparpa@gmail.com',
    url='http://github.com/csparpa/robograph',
    packages=['robograph',
              'robograph.datamodel',
              'robograph.datamodel.base',
              'robograph.datamodel.nodes',
              'robograph.datamodel.nodes.lib',
              'robograph.datamodel.tests',
              'sample_graphs'],
    long_description="""\
        Robograph is a platform that allows you to define your algorithms as computational graphs.
        Once you've defined the graph, you can execute that graph as if it was a SW
        program and get the expected outputs.
        As each algorithm is composed by steps, each graph is composed by nodes, each
        one being a step of the bigger calculation. Each graph can accept any number of
        inputs and give at maximum one output.
        You can create your own graphs either by connecting any of the predefined
        basic nodes shipped with Robograph or by coding your custom nodes
      """,
    classifiers=[
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
          "Topic :: Software Development :: Libraries",
    ],
    install_requires=[
        'cloudpickle==0.2.1',
        'jsonpickle==0.9.3',
        'networkx==1.11',
        'requests==2.10.0'
    ],
    keywords='robograph graph node engine computing',
    license='MIT',
    test_suite='datamodel.tests'
)
