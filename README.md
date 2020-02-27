# CovParser

## Installation
```shell
python setup.py install
```

## Cobertura format
```python
from cov_parser import cobertura
cobertura("example.xml")
```

In Cobertura, one `.xml` file contains coverage results for multiple files.

Output:
```python
{
  "file1": {1: 0, 2: 1, ....}, # a key is a line number 
  "file2": {1: 1, 2: 1, ....},
}
```

> Tips 🐙! `coverage.py`, a coverage measurement tool for Python, also produce an Cobertura-compatible XML report. Just use `coverage xml` instead of `coverage report` or `coverage html`.


## Gcov format
```python
from cov_parser import gcov
gcov("example.gcov")
```

In Gcov, a `.gcov` file is created for each `.c` source file.

Output:
```python
{1: 0, 2: 1, ....}, # a key is a line number 
```

## Note that
- Lines not appeared in the output dict are uncoverable lines.
