# pyTemplate

A template for building a python pkg

| **Documentation** | **Build Status** | **Coverage** |
|:-----------------:|:----------------:|:------------:|
| [![doc badge]][doc link] <br> [![website badge]][website link] | [![CI badge]][CI link] | [![codecov badge]][codecov link] <br> [![codecov graph]][codecov link] |

[doc badge]: https://github.com/quantaser/pytemplate/actions/workflows/Docs.yml/badge.svg
[doc link]: https://github.com/quantaser/pytemplate/actions/workflows/Docs.yml

[website badge]: https://img.shields.io/website?url=https%3A%2F%2Fquantaser.github.io%2Fpytemplate%2F
[website link]: https://quantaser.github.io/pytemplate/

[ci badge]: https://github.com/quantaser/pytemplate/actions/workflows/CI.yml/badge.svg
[ci link]: https://github.com/quantaser/pytemplate/actions/workflows/CI.yml

[codecov badge]: https://codecov.io/gh/quantaser/pytemplate/branch/main/graph/badge.svg?token=9KLNCETIYB
[codecov link]: https://codecov.io/gh/quantaser/pytemplate
[codecov graph]: https://codecov.io/gh/quantaser/pytemplate/branch/main/graphs/sunburst.svg?token=9KLNCETIYB

## Installation

To install this package, simply run:

```bash
$ pip install --upgrade git+https://github.com/quantaser/pytemplate.git

```

## Quick start

Import `Rock-Paper-Scissors Game` module:

```python
>>> import pytemplate.rock_paper_scissors as rps
```

Declare some `Gesture`

```python
>>> g0 = rps.Gesture(0)
>>> g0
scissor
>>> g1 = rps.Gesture(1)
>>> g1
rock
>>> g2 = rps.Gesture(2)
>>> g2
paper
```

Compare the `Gesture`s

```python
>>> g0.compare(g1)
'loss'
>>> g0.compare(g2)
'win'
>>> g1.compare(g0)
'win'
>>> g1.compare(g2)
'loss'
>>> g2.compare(g0)
'loss'
>>> g2.compare(g1)
'win'
```

> **Note**
> The functions under `untested` module are not tested yet.
