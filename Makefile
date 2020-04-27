#
# Minimal makefile for Sphinx documentation based on
# doxygen + breath-apidoc + sphinx-apidoc + sphinx-build
#

# You can set these variables from the command line.
DOC_BUILD_DIR        = _build/docs

# Doxygen
DOXYGEN         = doxygen

# Sphinx
SPHINXOPTS      =
SPHINX_APIDOC   = sphinx-apidoc
SPHINX_BUILD    = sphinx-build
SPHINX_QUIET	= #-Q
SPHINX_BUILD_IN = $(DOC_BUILD_DIR)/sphinx
SPHINX_BUILD_OUT = $(SPHINX_BUILD_IN)

# Breathe extension
BREATHE_APIDOC  = breathe-apidoc
BREATHE_IN      = $(DOC_BUILD_DIR)/doxygen/xml
BREATHE_OUT     = $(SPHINX_BUILD_OUT)/breathe
BREATHE_OPTION  = -g union,namespace,class,group,struct,file,interface

all:
	make html

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
	$(DOXYGEN) doc_config_files/doxygen/Doxyfile

	# Generate the .rst files from the doxygen xml output
	$(BREATHE_APIDOC) -o $(BREATHE_OUT) $(BREATHE_IN) $(BREATHE_OPTION) 

	# Generate the python API .rst files
	$(SPHINX_APIDOC) -o $(SPHINX_BUILD_OUT) python/sphinx_tuto
	
	# Copy the config files
	cp -r doc_config_files/sphinx/* $(DOC_BUILD_DIR)/sphinx

	#copy the markdown doc files
	cd $(DOC_BUILD_DIR)/sphinx && ln -sf ../../../doc && cd -

	# Generate the final layout.
	@$(SPHINX_BUILD) -M $@ "$(SPHINX_BUILD_IN)" "$(SPHINX_BUILD_OUT)" $(SPHINXOPTS) $(O) $(SPHINX_QUIET)