Parse markdown properly with sphinx
===================================

In order to parse the markdown properly one needs to add the following lines to
the config.py.
See the [Sophinx documentation](https://docs.readthedocs.io/en/latest/intro/getting-started-with-sphinx.html#using-markdown-with-sphinx).

First install the markdown parser for Sphinx:

~~~bash
pip3 install recommonmark
~~~

Then add the parser to the sphinx configuration:

~~~python
# Parse markdown properly.
from recommonmark.parser import CommonMarkParser
source_parsers = {
    '.md': CommonMarkParser,
}

# The suffix(es) of source filenames.
source_suffix = ['.rst', '.md']
~~~

Enjoy.