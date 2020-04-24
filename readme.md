Readme
======

## sphinx_tuto

Small project to see how to build the documentation of an hybrid project
C++/python/markdown

## Getting started

In order to build the documentation of the package one can use CMake or the
Makefile directly.

### Using CMake

The classic way of using CMake is the following after changing directory
to this package:

    mkdir _build
    cd _build
    cmake ..
    make
    firefox devel/share/docs/sphinx/html/index.html

### Using Makefile

The make file is a simplified version of the CMakeLists.txt

    make
    firefox _build/docs/sphinx/html/index.html

## Advanced explanation on the tools

In order to build the documentation we need to setup the following tools:
- [Doxygen](http://www.doxygen.nl/) the C++ api documentation parser,
- [Breathe](https://breathe.readthedocs.io/en/latest/) a sphinx extension that
    parse the doxygen xml output into restructured text files,
- [recommonmark](https://recommonmark.readthedocs.io/en/latest/) a sphinx
    extension parsing markdown files.
- [sphinx-apidoc](http://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html)
    the Python api documentation parser,
- [Sphinx](http://www.sphinx-doc.org/en/master/) the documentation renderer,

### Setup Doxygen

#### With CMake

#### With Makefile

------------------------

### Setup Breath

#### With CMake

#### With Makefile

------------------------

### Setup recommonmark

#### With CMake

#### With Makefile

------------------------

### Setup Sphinx-apidoc

#### With CMake

#### With Makefile

------------------------

### Setup Sphinx

#### With CMake

#### With Makefile