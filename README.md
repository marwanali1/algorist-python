# Algorist Python

[![Build Status](https://github.com/marwanali1/algorist-python/actions/workflows/ci.yml/badge.svg)](https://github.com/marwanali1/algorist-python/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-MIT-gr.svg)](https://github.com/marwanali1/algorist-python/blob/main/LICENSE)

A library of commonly used data structures, algorithms, and design patterns implemented in Python.

## Getting Started

#### Run in Python REPL:
`cd algorist-python`  
`python3`  
`>>> from src.data_structures.hashtable import HashTable`  
`>>> hashtable = HashTable()`  
`>>> hashtable.put("one", 1)`  
`>>> print(hashtable)`  
`{'one': 1}`

#### Run Source File:
`python3 src/data_structures/hashtable.py`  

#### Run a single test file:
`python3 -m unittest tests/data_structures/test_hashtable.py`

#### Run all tests:
`python3 -m unittest discover`