# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
DOXYGEN       = doxygen
DOXYREST      = doxyrest
SPHINXOPTS    =
SPHINX_APIDOC = sphinx-apidoc
SPHINXBUILD   = sphinx-build
SOURCEDIR     = build/sphinx_tuto/docs
BUILDDIR      = build/sphinx_tuto/

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	# Create the build folder if it does not exists.
	mkdir -p $(BUILDDIR)
	# Configure/copy the docs parameters
	cp -fr docs $(BUILDDIR)

	# Generate the doxygen (xml) symbols
	cd $(SOURCEDIR) ; $(DOXYGEN) Doxyfile ; cd -

	# Generate the .rst from the Dpxygen (xml) symbols
	# cd $(SOURCEDIR) ; doxyrest doxyoutput/xml/index.xml -o doxyrest_out/index.rst --frame=index_main.rst.in --frame-dir=/home/mnaveau/Software/install/share/cfamily --frame-dir=/home/mnaveau/Software/install/share/common ; cd -

	# Generate the python API .rst files
	$(SPHINX_APIDOC) -o $(SOURCEDIR) python/sphinx_tuto
	
	# Generate the final layout.
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)