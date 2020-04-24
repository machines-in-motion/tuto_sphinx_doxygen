# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
DOC_BUILD_DIR        = _build/docs

DOXYGEN         = doxygen
BREATHE_APIDOC  = breathe-apidoc
BREATHE_IN      = $(DOC_BUILD_DIR)/doxygen/xml
BREATHE_OUT     = $(DOC_BUILD_DIR)/breath
BREATHE_OPTION  = -g union,namespace,class,group,struct,file,interface
# DOXYREST        = doxyrest
SPHINXOPTS      =
SPHINX_APIDOC   = sphinx-apidoc
SPHINX_BUILD    = sphinx-build
SPHINX_BUILD_IN = $(DOC_BUILD_DIR)
SPHINX_BUILD_OUT = $(DOC_BUILD_DIR)/sphinx


# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINX_BUILD) -M help "$(SPHINX_BUILD_IN)" "$(DOC_BUILD_DIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	# Create the build folder if it does not exists.
	mkdir -p $(DOC_BUILD_DIR)
	mkdir -p $(SPHINX_BUILD_OUT)
	mkdir -p $(BREATHE_OUT)

	# Generate the doxygen (xml) symbols
	$(DOXYGEN) doc_config_files/doxygen/Doxyfile.in

	# Generate the .rst from the Dpxygen (xml) symbols
	# cd $(SOURCEDIR) ; doxyrest doxyoutput/xml/index.xml -o doxyrest_out/index.rst --frame=index_main.rst.in --frame-dir=/home/mnaveau/Software/install/share/cfamily --frame-dir=/home/mnaveau/Software/install/share/common ; cd -

	# Generate the .rst files from the doxygen xml output
	$(BREATHE_APIDOC) -o $(BREATHE_OUT) $(BREATHE_IN) $(BREATHE_OPTION) 

	# Generate the python API .rst files
	$(SPHINX_APIDOC) -o $(DOC_BUILD_DIR) python/sphinx_tuto
	
	# Copy the config files
	cp -r doc_config_files/sphinx/* $(DOC_BUILD_DIR)/sphinx

	# Generate the final layout.
	@$(SPHINX_BUILD) -M $@ "$(SPHINX_BUILD_IN)" "$(SPHINX_BUILD_OUT)" $(SPHINXOPTS) $(O)