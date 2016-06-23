# Robograph
A graph-oriented algorithmic engine

## Install dependencies
`sudo pip install -r requirements.txt`

## Executing some graphs

Import any factory from `sample_graphs`, then instantiate and execute.
Eg:

```
from sample_graphs import sum_and_product
graph = sum_and_product.sum_and_product([3, 4, 5])
output = graph.execute()
print output # sum is: 12, product is: 60
```


## Developing/testing 

### Install dev dependencies
`sudo pip install -r dev-requirements.txt`

### Unit tests
`py.test datamodel/tests`
